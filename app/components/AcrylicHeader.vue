<script setup lang="ts">

const links = [
  { label: '首页', to: '/' },
  { label: '还在制作力', to: '/qwq' }
]

const drawerOpen = ref(false)
</script>

<template>
  <header
    class="sticky top-0 z-50 flex h-16 items-center justify-between
           bg-white/70 dark:bg-gray-900/70 backdrop-blur-md shadow-lg
           px-4 md:px-8 transition-colors"
  >
    <!-- Logo -->
    <NuxtLink to="/" class="text-xl font-bold text-gray-800 dark:text-white">
      辰砂屿
    </NuxtLink>

    <!-- 桌面导航 -->
    <nav class="hidden md:flex items-center gap-6">
      <NuxtLink
      v-for="link in links"
      :key="link.to"
      :to="link.to"
      :class="[
        'text-sm font-medium transition-colors',
        $route.path === link.to
          ? 'text-primary font-bold'
          : 'text-gray-700 dark:text-gray-300 hover:text-primary'
      ]"
    >
        {{ link.label }}
      </NuxtLink>
    </nav>

    <div class="flex items-center gap-4">
      <ColorModeButton />
      <button
        class="md:hidden text-gray-600 dark:text-gray-300"
        @click="drawerOpen = !drawerOpen"
      >
        <Icon name="lucide:menu" class="h-6 w-6" />
      </button>
    </div>
  </header>

  <Transition
    enter-active-class="duration-200 ease-out"
    enter-from-class="opacity-0 -translate-y-2"
    enter-to-class="opacity-100 translate-y-0"
    leave-active-class="duration-150 ease-in"
    leave-from-class="opacity-100 translate-y-0"
    leave-to-class="opacity-0 -translate-y-2"
  >
    <nav
      v-show="drawerOpen"
      class="md:hidden fixed top-16 left-0 right-0 z-40
             bg-white/80 dark:bg-gray-900/80 backdrop-blur-md
             flex flex-col gap-4 p-4 shadow-lg"
    >
      <NuxtLink
      v-for="link in links"
      :key="link.to"
      :to="link.to"
      :class="[
        'block py-2 text-sm font-medium transition-colors',
        $route.path === link.to
          ? 'text-primary font-bold'
          : 'text-gray-700 dark:text-gray-300 hover:text-primary'
      ]"
      @click="drawerOpen = false"
    >
        {{ link.label }}
      </NuxtLink>
    </nav>
  </Transition>
</template>