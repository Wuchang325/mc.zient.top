<template>
  <footer
    class="fixed bottom-0 left-0 right-0 backdrop-blur-md bg-white/70 dark:bg-gray-900/70 shadow-inner
           p-4 border-t border-gray-200 dark:border-gray-700"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <!-- 版权信息 -->
        <div>
          <p class="text-sm text-gray-700 dark:text-gray-300">
            &copy; {{ new Date().getFullYear() }} 辰砂屿 版权所有
          </p>
        </div>

        <!-- 备案信息 -->
        <div>
          <p class="text-sm text-gray-700 dark:text-gray-300">
            <a
              href="https://beian.miit.gov.cn/"
              target="_blank"
              class="hover:text-primary"
            >
              冀ICP备2025114767号-1
            </a>
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>