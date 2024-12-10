<script>
  import { Link } from "svelte-routing";
  let isOpen = true;

  function toggleNavbar() {
    isOpen = !isOpen;
  }
  function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }
</script>

<div class="flex h-screen overflow-hidden ml-4 mr-4 w-full pt-24">
  <!-- Sidebar -->
  <aside
    class="bg-[#1E2875] text-white h-screen transition-all duration-300 overflow-x-visible overflow-y-auto relative items-center pt-4"
    class:w-64={isOpen}
    class:w-32={!isOpen}
  >
    <div class="p-6 flex items-center justify-between">
      <h1 class="text-2xl font-bold whitespace-nowrap" class:hidden={!isOpen}>Menu</h1>
      <button
        on:click={toggleNavbar}
        class="text-white p-2 rounded-full hover:bg-blue-800 transition-colors absolute"
        class:right-0={isOpen}
        class:right-[0px]={!isOpen}
        class:top-[32px]={!isOpen}
      >
        {#if isOpen}
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 19l-7-7 7-7m8 14l-7-7 7-7" />
          </svg>
        {:else}
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7" />
          </svg>
        {/if}
      </button>
    </div>
    <nav class="mt-6">
      {#each [
        { to: "/dashboard", icon: "fas fa-home", label: "Dashboard" },
        { to: "/profile", icon: "fas fa-user", label: "Profile" },
        { to: "/assessments", icon: "fas fa-clipboard", label: "Assessments" },
        { to: "/mitra", icon: "fas fa-brain", label: "Mitra" },
        { to: "/mylearnings", icon: "fas fa-chart-line", label: "My Learnings" },
        { to: "/feedback", icon: "fas fa-comments", label: "Feedback" }
      ] as item}
        <Link 
          to={item.to} 
          class="flex gap-4 px-16 py-3 hover:bg-blue-800 transition-colors"
        >
          <i class="{item.icon} w-5 h-5 flex-shrink-0"></i>
          {#if isOpen}
            <span class="whitespace-nowrap">{item.label}</span>
          {/if}
        </Link>
      {/each}
    </nav>
  </aside>

  <div class="flex-1 flex flex-col overflow-hidden">
    <!-- Top Navigation Bar -->
    <nav class="bg-[#1E2875] text-white fixed top-0 left-4 right-4 z-50 py-2 pr-8">
      <div class="container mx-auto flex justify-between items-center px-4">
        <img src="\logom.png" alt="Logo" class="h-24 pt-4 pl-4" />
        <div class="flex flex-col items-center">
          <h1 class="text-3xl font-bold">Welcome Back!</h1>
        </div>
        <div class="space-x-8">
          <a href="/" class="hover:text-blue-200 transition-colors">Home</a>
          <a href="/" class="hover:text-blue-200 transition-colors">Services</a>
          <a href="/" class="hover:text-blue-200 transition-colors">About Us</a>
          <a href="/" class="hover:text-blue-200 transition-colors">Contact Us</a>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-1 overflow-x-hidden overflow-y-auto bg-[#FDF8EE]">
      <div class="container mx-auto px-6 py-8">
        <slot />
      </div>
    </main>
  </div>
</div>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    scroll-behavior: smooth;
  }

  aside {
    position: relative;
    z-index: 10;
  }

  button {
    border: none;
    outline: none;
  }
</style>

