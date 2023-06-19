
export default {
  dev: {
    '/api/xadmin/v1/': {
      target: 'http://127.0.0.1:8000',
      changeOrigin: true,
      pathRewrite: {
        '/api/xadmin/v1/': '/api/xadmin/v1/',
      },
    },
  },
  test: {
    '/api/': {
      changeOrigin: true,
      pathRewrite: {
        '^': '',
      },
    },
  },
  pre: {
    '/api/': {
      target: 'your pre url',
      changeOrigin: true,
      pathRewrite: {
        '^': '',
      },
    },
  },
};
