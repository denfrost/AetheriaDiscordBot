const response = await fetch('https://AetheriaDiscordBot.agentlonestar.repl.co/static/version.txt');
const version = await response.text();

$('body').terminal({
  test: function() {
    this.echo('Test')
    }
}, {
  greetings: 'Pointy-Haired Bot Control Console\nVersion ' + version + '\nCopyright AgentLoneStar007, All Rights Reserved\n',
  prompt: '>>> '
});

