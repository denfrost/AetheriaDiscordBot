$('body').terminal({
  test: function() {
    this.echo('Test')
    }
}, {
  greetings: 'Hello,',
  prompt: '>>> '
});

