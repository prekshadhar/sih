<script>
  import { Link, navigate } from "svelte-routing";
  import { isLoggedIn } from '../store'; 
  import { onMount } from 'svelte';

  let email = "";
  let username = "";
  let password = "";
  let isSignUp = true;

  function handleSubmit() {
    const isAuthenticated = email && password;

    if (isAuthenticated) {
      console.log(isSignUp ? "Sign Up" : "Sign In", { email, username, password });
      isLoggedIn.set(true);
      navigate("/dashboard");
    } else {
      alert("Please provide valid credentials!");
    }
  }

  function toggleForm() {
    isSignUp = !isSignUp;
  }

  function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }

  onMount(() => {
    const hash = window.location.hash;
    if (hash) {
      const sectionId = hash.substring(1);
      scrollToSection(sectionId);
    }

    // Add click event listeners to navigation links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const sectionId = link.getAttribute('href').substring(1);
        scrollToSection(sectionId);
      });
    });
  });
</script>

<div class="ml-2 mr-2 w-full">
  <nav class="bg-[#1E2875] text-peach-cream fixed top-0 left-4 right-4 z-50 py-2 pr-8">
    <div class="container mx-auto flex justify-between items-center px-4">
      <img src="\logom.png" alt="Logo" class="h-24 pt-4 pl-4" />
      <div class="flex flex-col items-center">
        <h1 class="text-3xl italic font-bold">Nirdeshika</h1>
        <p class="text-sm italic pl-48 pt-21">Your path, your journey – free from judgment.</p>
      </div>
      <div class="space-x-8">
        <a href="#auth" class="hover:text-blue-200 transition-colors">Home</a>
        <a href="#services" class="hover:text-blue-200 transition-colors">Services</a>
        <a href="#about" class="hover:text-blue-200 transition-colors">About Us</a>
        <a href="#contact" class="hover:text-blue-200 transition-colors">Contact Us</a>
      </div>
    </div>
  </nav>

  <section id="auth" class="bg-[#1E2875] text-white pb-32 relative overflow-hidden flex items-center justify-center">
    <!-- Decorative Elements -->
    <div class="absolute left-24 bottom-12">
      <img src="/cut.png" alt="" class="h-full w-72" />
    </div>
    <div class="absolute right-24 top-28">
      <img src="/rb.png" alt="" class="h-full w-72" />
    </div>

    <!-- Auth Form -->
    <div class="container pt-36 relative z-10 flex flex-col items-center">
      <h1 class="text-4xl font-bold mb-8 text-center">Welcome,</h1>
      <div class="backdrop-blur-md bg-white/10 rounded-lg p-8 w-full max-w-md border border-white/20">
        <form on:submit|preventDefault={handleSubmit} class="space-y-6">
          <h2 class="text-2xl font-semibold mb-6 text-center">{isSignUp ? 'SIGN UP!' : 'LOGIN!'}</h2>
          <div class="space-y-4">
            <input 
              type="email" 
              bind:value={email} 
              placeholder="ENTER EMAIL ADDRESS" 
              required 
              class="w-full px-4 py-3 bg-white/10 border border-white/30 rounded-md text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-white/50"
            />
            {#if isSignUp}
              <input 
                type="text" 
                bind:value={username} 
                placeholder="ENTER USERNAME" 
                required 
                class="w-full px-4 py-3 bg-white/10 border border-white/30 rounded-md text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-white/50"
              />
            {/if}
            <input 
              type="password" 
              bind:value={password} 
              placeholder="PASSWORD" 
              required 
              class="w-full px-4 py-3 bg-white/10 border border-white/30 rounded-md text-white placeholder-white/70 focus:outline-none focus:ring-2 focus:ring-white/50"
            />
            <button 
              type="submit" 
              class="w-full bg-white/20 hover:bg-white/30 text-white py-3 rounded-md transition-colors font-semibold backdrop-blur-sm"
            >
              {isSignUp ? 'Sign Up' : 'Sign In'}
            </button>
            <p class="text-center text-sm">
              {isSignUp ? 'Already a user?' : "Don't have an account?"} 
              <button type="button" on:click={toggleForm} class="text-white/90 hover:text-white hover:underline ml-1 transition-colors">
                {isSignUp ? 'Login' : 'Sign Up'}
              </button>
            </p>
          </div>
        </form>
      </div>
    </div>
  </section>

  <section id="services" class="bg-[#FDF8EE] px-8">
    <div class="container mx-auto">
      <div class="flex items-start gap-12">
        <div class="flex-1">
          <div class="absolute">
            <img src="/2a.png" alt="" class="h-full w-72" />
          </div>
          <h2 class="text-3xl font-bold text-[#1E2875] mb-6 pt-48 pl-36">What we do?</h2>
          <p class="text-gray-700 leading-relaxed max-w-2xl pl-52">
            We help students assess their academic level by conducting personalized tests. After evaluating their performance, we provide a detailed roadmap and review to highlight their strengths and areas for improvement.
            <br><br>
            Along with this, we offer tailored study materials to help them enhance their skills and achieve their full potential. Our goal is to guide students on their learning journey, providing the support they need to grow and succeed academically.
          </p>
        </div>
        <div class="flex-1 absolute right-6">
          <img src="public\student.png" alt="Student" class="w-full pt-8" />
          <!-- <div class="absolute bottom-0 right-0 w-32 h-32 bg-[#00BA9D] rounded-tl-3xl" />
        </div> -->
      </div>
    </div>
  </section>

  <section id="about" class="bg-[#FDF8EE] py-20 px-8">
    <div class="container mx-auto">
      <div class="flex flex-row-reverse items-start gap-12">
        <div class="flex-1">
          <h2 class="text-3xl font-bold text-[#1E2875] mb-2 pt-20">Who are we?</h2>
          <p class="text-gray-700 leading-relaxed pr-52 pl-14 content-end">
            Hi! We're a team of six students from Usha Mittal Institute of Technology, SNDT Women's University, united by a passion for making learning simple, enjoyable, and accessible. This website is our SIH Hackathon project, designed to create a platform that empowers learners from all backgrounds.
            <br><br>
            Our mission is to make education fun and engaging with an intuitive, user-friendly platform. With our diverse skills in web development, design, and content creation, we're building a space that evolves with your learning needs. Join us on this exciting journey toward accessible, interactive, and enjoyable learning!
          </p>
        </div>
        <div class="flex-1 relative">
          <img src="/us.png" alt="team" class="pl-24" />
        </div>
        <div class="flex-1 absolute right-4">
          <img src="/st1.png" alt="" class="w-full" />
        </div>
        <div class="flex-1 absolute right">
          <img src="/star.png" alt="" class="w-full pt-60" />
        </div>
      </div>
    </div>
  </section>

  <section id="contact" class="bg-[#1E2875] text-white py-12">
    <div class="container mx-auto px-8">
      <h2 class="text-3xl font-bold mb-8">CONTACT US</h2>
      <div class="flex justify-center space-x-8">
        <a href="mailto:contact@example.com" class="hover:text-blue-400 transition-colors">
          <i class="fas fa-envelope fa-2x"></i>
        </a>
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="hover:text-blue-400 transition-colors">
          <i class="fab fa-instagram fa-2x"></i>
        </a>
        <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="hover:text-blue-400 transition-colors">
          <i class="fab fa-linkedin-in fa-2x"></i>
        </a>
      </div>
    </div>
  </section>
</div>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
  }

  input::placeholder {
    text-transform: uppercase;
  }

  /* Add glass morphism effect */
  .backdrop-blur-md {
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
  }
</style>