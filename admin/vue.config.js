module.exports = {
  publicPath: "/",
  devServer: {
    proxy: {
      "/api": {
        target: "http://52.78.81.59:8000/"
      },
      "/static/posters": {
        target: "http://52.78.81.59:8000/"
      }
    }
  }
};
