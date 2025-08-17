// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  srcDir: 'app/',
  devtools: { enabled: true },
  modules: [
    '@nuxt/ui'
  ],
  css: [
    '@/assets/css/main.css'
  ],
  //ssr: true,       // 关闭服务端渲染
  //nitro: {
  //  prerender: {
  //    crawlLinks: false, // 关闭自动预抓取
  //    routes: []         // 不预渲染任何路由
  //  }
  //},
  ui: {
    fonts: false
  },
  app: {
    baseURL: 'https://mc.zient.top/',  // 设置应用的基础路径

    head: {
      titleTemplate: '%s | 辰砂屿'   // %s 会被当前页面标题替换
    }
  },
  nitro: {
    preset: 'github_pages'
  }
})

