module.exports = {
  // this path MUST match path in /public/404.html or GitHub Pages will not redirect URLs properly:
  publicPath: '/sounding-board-gladbeck/',
  productionSourceMap: true,
  chainWebpack: config => {
    /*
     * the default loaders for worker files must be disabled. Otherwise both the default and the loaders defined below
     * will be applied to worker files. See also: https://github.com/vuejs/vue-cli/issues/2028
     */
    config.module.rule('js').exclude.add(/\.worker\.js$/)
    config.module.rule('ts').exclude.add(/\.worker\.ts$/)

    config.module
      .rule('i18n')
      .resourceQuery(/blockType=i18n/)
      .type('javascript/auto')
      .use('i18n')
      .loader('@kazupon/vue-i18n-loader')
      .end()
      .use('yaml')
      .loader('yaml-loader')
      .end()
  },
  configureWebpack: {
    plugins: [],
    module: {
      rules: [
        {
          test: /\.md$/,
          use: [
            {
              loader: 'html-loader',
            },
            {
              loader: 'markdown-loader',
              options: {
                /* your options here */
              },
            },
          ],
        },
      ],
    },
  },
}
