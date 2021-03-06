module.exports = {
    devServer:{
        port:8080,
        host:"0.0.0.0",
        https:false,
        open:true,
        proxy:{  
            '/':{
                target:'http://127.0.0.1:8000/',
                changeOrigin:true,
                pathRewrite:{
                    "^/":""
                }
            }
        },
    },
 
    lintOnSave:false,
    productionSourceMap:false,
}