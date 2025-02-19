const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: "http://127.0.0.1:443/",
  //    publicPath: "/",
  outputDir: "./dist/",
  //    outputDir: '',

  chainWebpack: config => {
    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./dist/webpack-stats.json" }]);

    config.output.filename("bundle.js");

    config.optimization.splitChunks(false);

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public("http://127.0.0.1:443")
      .proxy("http://localhost:443")
      .host("0.0.0.0")
      .port(443)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  },

  css: {
    extract: {
      filename: "bundle.css",
      chunkFilename: "bundle.css"
    }
  }
};
