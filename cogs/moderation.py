
const {
  PermissionsBitField,
  EmbedBuilder
} = require("discord.js");

const fs = require("node:fs");

const PREFIX = process.env.PREFIX || "!";
const DATA_FILE = "./moderation-data.json";

function loadData() {
  try {
    return JSON.parse(fs.readFileSync(DATA_FILE, "utf8"));
  } catch {
    return {
      warnings: {},
      logs: {},
      blockedWords: [],
      blockedLinks: true,
      automodEnabled: true
    };
  }
}

let data = loadData();

function saveData() {
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

const spam = new Map();
const cooldowns = new Map();

async function sendLog(guild, title, description) {
  const id = data.logs[guild.id];
  if (!id) return;

  const channel = guild.channels.cache.get(id);
  if (!channel || !channel.isTextBased()) return;

  const embed = new EmbedBuilder()
    .setColor(0x5865F2)
    .setTitle(title)
    .setDescription(description.slice(0, 4000))
    .setTimestamp();

  await channel.send({ embeds: [embed] }).catch(() => {});
}

function getTarget(message, args) {
  const mentioned = message.mentions.members.first();

  if (mentioned) {
    return {
      member: mentioned,
      args: args.filter(a => !/^<@!?\d+>$/.test(a))
    };
  }

  const id = (args[0] || "").replace(/[<@!>]/g, "");

  if (/^\d{17,20}$/.test(id)) {
    return {
      member: message.guild.members.cache.get(id),
      args: args.slice(1)
    };
  }

  return { member: null, args };
}

function checkTarget(message, target) {
  if (!target) return "مش لاقي العضو.";
  if (target.id === message.author.id) return "مينفعش تعاقب نفسك.";
  if (target.id === message.guild.ownerId) return "مينفعش تعاقب صاحب السيرفر.";

  if (
    message.author.id !== message.guild.ownerId &&
    target.roles.highest.position >= message.member.roles.highest.position
  ) {
    return "رتبتك لازم تكون أعلى من رتبة العضو.";
  }

  if (!target.manageable) return "ارفع رتبة البوت فوق رتبة العضو.";
  return null;
}

async function say(message, text) {
  return message.reply({
    content: text.slice(0, 1900),
    allowedMentions: { repliedUser: false }
  }).catch(() => {});
}

function setupModeration(client) {
  client.on("messageCreate", async message => {
    if (!message.guild || message.author.bot) return;

    const isMod = message.member.permissions.has(
      PermissionsBitField.Flags.ManageMessages
    );

    // Auto moderation
    if (data.automodEnabled && !isMod) {
      const now = Date.now();
      const key = `${message.guild.id}:${message.author.id}`;

      const recent = (spam.get(key) || [])
        .filter(t => now - t < 7000);

      recent.push(now);
      spam.set(key, recent);

      if (recent.length >= 6) {
        await message.delete().catch(() => {});

        const member = await message.guild.members
          .fetch(message.author.id).catch(() => null);

        if (member?.moderatable) {
          await member.timeout(60_000, "AutoMod spam")
            .catch(() => {});
        }

        await sendLog(
          message.guild,
          "Anti-Spam",
          `${message.author.tag} اتعمله إجراء بسبب السبام.`
        );

        return;
      }

      const content = message.content.toLowerCase();

      const blockedWord = data.blockedWords.find(
        word => content.includes(word.toLowerCase())
      );

      const hasLink =
        /(https?:\/\/|www\.|discord\.gg\/)/i.test(message.content);

      if (blockedWord || (data.blockedLinks && hasLink)) {
        await message.delete().catch(() => {});

        await sendLog(
          message.guild,
          "AutoMod Filter",
          `رسالة محذوفة من ${message.author.tag}`
        );

        return;
      }
    }

    if (!message.content.startsWith(PREFIX)) return;

    const parts = message.content
      .slice(PREFIX.length).trim().split(/\s+/);

    const command = (parts.shift() || "").toLowerCase();
    const args = parts;

    if (!command) return;

    const cdKey = `${message.author.id}:${command}`;
    if (Date.now() - (cooldowns.get(cdKey) || 0) < 1000) return;
    cooldowns.set(cdKey, Date.now());

    const hasPerm = permission =>
      message.member.permissions.has(permission);

    const ADMIN = PermissionsBitField.Flags.Administrator;
    const MOD = PermissionsBitField.Flags.ModerateMembers;
    const MANAGE_MESSAGES = PermissionsBitField.Flags.ManageMessages;
    const MANAGE_CHANNELS = PermissionsBitField.Flags.ManageChannels;

    if (command === "modhelp") {
      return say(message,
`**777 Moderation**
\`!ban @عضو السبب\`
\`!kick @عضو السبب\`
\`!timeout @عضو دقائق السبب\`
\`!untimeout @عضو\`
\`!warn @عضو السبب\`
\`!warnings @عضو\`
\`!clearwarnings @عضو\`
\`!clear عدد\`
\`!lock\` / \`!unlock\`
\`!slowmode ثواني\`
\`!setlogs\`
\`!blocklink on/off\`
\`!blockword add/remove كلمة\`
\`!automod on/off\``);
    }

    if (command === "setlogs") {
      if (!hasPerm(ADMIN)) return say(message, "الأمر للأدمن بس.");

      data.logs[message.guild.id] = message.channel.id;
      saveData();

      return say(message, "تم تعيين القناة دي للـ Logs.");
    }

    if (command === "ban" || command === "kick") {
      const permission = command === "ban"
        ? PermissionsBitField.Flags.BanMembers
        : PermissionsBitField.Flags.KickMembers;

      if (!hasPerm(permission)) return say(message, "معندكش الصلاحية.");

      const parsed = getTarget(message, args);
      const target = parsed.member;
      const error = checkTarget(message, target);

      if (error) return say(message, error);

      const reason = parsed.args.join(" ") || "بدون سبب";

      if (command === "ban") {
        if (!target.bannable) return say(message, "مش قادر أعمل Ban للعضو.");

        await target.ban({
          reason: `${message.author.tag}: ${reason}`
        });
      } else {
        if (!target.kickable) return say(message, "مش قادر أعمل Kick للعضو.");

        await target.kick(`${message.author.tag}: ${reason}`);
      }

      await say(message, `تم ${command} للعضو **${target.user.tag}**. السبب: ${reason}`);

      return sendLog(
        message.guild,
        `Member ${command}`,
        `${target.user.tag}\nبواسطة: ${message.author.tag}\nالسبب: ${reason}`
      );
    }

    if (command === "timeout" || command === "untimeout") {
      if (!hasPerm(MOD)) return say(message, "معندكش الصلاحية.");

      const parsed = getTarget(message, args);
      const target = parsed.member;
      const error = checkTarget(message, target);

      if (error) return say(message, error);
      if (!target.moderatable) return say(message, "مش قادر أعدل حالة العضو.");

      if (command === "untimeout") {
        await target.timeout(null);
        return say(message, `اتشال الـ Timeout عن ${target.user.tag}.`);
      }

      const minutes = Number(parsed.args[0]);

      if (!Number.isInteger(minutes) || minutes < 1 || minutes > 40320) {
        return say(message, "اكتب عدد الدقايق من 1 لـ 40320.");
      }

      const reason = parsed.args.slice(1).join(" ") || "بدون سبب";

      await target.timeout(minutes * 60000, reason);

      await say(message, `اتعمل Timeout لـ ${target.user.tag} لمدة ${minutes} دقيقة.`);

      return sendLog(
        message.guild,
        "Timeout",
        `${target.user.tag}\nالمدة: ${minutes} دقيقة\nالسبب: ${reason}`
      );
    }

    if (command === "warn") {
      if (!hasPerm(MOD)) return say(message, "معندكش الصلاحية.");

      const parsed = getTarget(message, args);
      const target = parsed.member;
      const error = checkTarget(message, target);

      if (error) return say(message, error);

      const reason = parsed.args.join(" ");
      if (!reason) return say(message, "اكتب سبب التحذير.");

      const key = `${message.guild.id}:${target.id}`;

      data.warnings[key] ||= [];
      data.warnings[key].push({
        reason,
        moderator: message.author.id,
        date: Date.now()
      });

      saveData();

      await say(message,
        `⚠️ اتحذر ${target.user.tag}. إجمالي التحذيرات: ${data.warnings[key].length}`
      );

      return sendLog(
        message.guild,
        "Warning",
        `${target.user.tag}\nالسبب: ${reason}\nبواسطة: ${message.author.tag}`
      );
    }

    if (command === "warnings" || command === "clearwarnings") {
      if (!hasPerm(command === "clearwarnings" ? ADMIN : MOD)) {
        return say(message, "معندكش الصلاحية.");
      }

      const target = getTarget(message, args).member;
      if (!target) return say(message, "منشن العضو.");

      const key = `${message.guild.id}:${target.id}`;

      if (command === "clearwarnings") {
        data.warnings[key] = [];
        saveData();
        return say(message, `اتمسحت تحذيرات ${target.user.tag}.`);
      }

      const warnings = data.warnings[key] || [];

      if (!warnings.length) {
        return say(message, "العضو ده معندوش تحذيرات.");
      }

      return say(message, warnings.map((w, i) =>
        `${i + 1}. ${w.reason} | بواسطة <@${w.moderator}>`
      ).join("\n"));
    }

    if (command === "clear") {
      if (!hasPerm(MANAGE_MESSAGES)) return say(message, "معندكش الصلاحية.");

      const amount = Number(args[0]);

      if (!Number.isInteger(amount) || amount < 1 || amount > 100) {
        return say(message, "اكتب رقم من 1 لـ 100.");
      }

      const deleted = await message.channel
        .bulkDelete(amount + 1, true).catch(() => null);

      if (!deleted) {
        return say(message, "فشل المسح. راجع الصلاحيات وعمر الرسائل.");
      }

      return sendLog(
        message.guild,
        "Clear",
        `${message.author.tag} مسح ${deleted.size - 1} رسالة.`
      );
    }

    if (command === "lock" || command === "unlock") {
      if (!hasPerm(MANAGE_CHANNELS)) return say(message, "معندكش الصلاحية.");

      const locked = command === "lock";

      await message.channel.permissionOverwrites.edit(
        message.guild.roles.everyone,
        { SendMessages: locked ? false : null }
      );

      return say(message, locked ? "🔒 الشات اتقفل." : "🔓 الشات اتفتح.");
    }

    if (command === "slowmode") {
      if (!hasPerm(MANAGE_CHANNELS)) return say(message, "معندكش الصلاحية.");

      const seconds = Number(args[0]);

      if (!Number.isInteger(seconds) || seconds < 0 || seconds > 21600) {
        return say(message, "اكتب رقم من 0 لـ 21600 ثانية.");
      }

      await message.channel.setRateLimitPerUser(seconds);
      return say(message, `تم ضبط Slowmode على ${seconds} ثانية.`);
    }

    if (command === "blocklink") {
      if (!hasPerm(ADMIN)) return say(message, "الأمر للأدمن بس.");

      if (!["on", "off"].includes(args[0])) {
        return say(message, "استخدم !blocklink on أو !blocklink off");
      }

      data.blockedLinks = args[0] === "on";
      saveData();

      return say(message, `فلتر الروابط ${data.blockedLinks ? "اشتغل" : "اتقفل"}.`);
    }

    if (command === "blockword") {
      if (!hasPerm(ADMIN)) return say(message, "الأمر للأدمن بس.");

      const action = args.shift();
      const word = args.join(" ").toLowerCase().trim();

      if (!["add", "remove"].includes(action) || !word) {
        return say(message, "استخدم !blockword add كلمة أو !blockword remove كلمة");
      }

      if (action === "add" && !data.blockedWords.includes(word)) {
        data.blockedWords.push(word);
      }

      if (action === "remove") {
        data.blockedWords = data.blockedWords.filter(w => w !== word);
      }

      saveData();
      return say(message, "تم تحديث قائمة الكلمات المحظورة.");
    }

    if (command === "automod") {
      if (!hasPerm(ADMIN)) return say(message, "الأمر للأدمن بس.");

      if (!["on", "off"].includes(args[0])) {
        return say(message, "استخدم !automod on أو !automod off");
      }

      data.automodEnabled = args[0] === "on";
      saveData();

      return say(message, `AutoMod ${data.automodEnabled ? "اشتغل" : "اتقفل"}.`);
    }
  });
}

module.exports = { setupModeration };
