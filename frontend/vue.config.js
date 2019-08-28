module.exports = {
  publicPath: '/',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000/',
      },
      '/static/posters': {
        target: 'http://localhost:8000/',
      },
    }
  }
}