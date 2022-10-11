const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath:"./",
  devServer:{
    port:10086,
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    // allowedHosts:[
    //   'jluyyds.ltd',
    //   '*.jluyyds.ltd',
    // ],
    historyApiFallback: {
      index: '/'
    },
    proxy:{
      // '/api':{
      //   target: 'https://github.com/',// 后端接口
      //   changeOrigin: true, // 是否跨域
      //   secure:false,
      //   pathRewrite: {
      //     '/api': ''
      //   }
      // }
    }
	}
})
