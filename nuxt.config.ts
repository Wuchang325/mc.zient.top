export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  srcDir: 'app/',
  devtools: { enabled: true },
  modules: ['@nuxt/ui'],
  css: ['@/assets/css/main.css'],
  app: {
    baseURL: '/',
    head: {
      titleTemplate: '%s | 辰砂屿'
    }
  },
  nitro: {
    preset: 'github_pages',
    prerender: {
      routes: ['/404.html', '/200.html']
    }
  }
})