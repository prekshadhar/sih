<script>
  import { Link, navigate } from "svelte-routing";
  import { isLoggedIn } from '../store'; 

  let email = "";
  let username = "";
  let password = "";
  let isSignUp = true;

  function handleSubmit() {
    // console.log(isSignUp ? "Sign Up" : "Sign In", { email, username, password });
  
    // if (isSignUp) {
    const isAuthenticated = email && password; // Replace with your backend validation logic

    if (isAuthenticated) {
      console.log(isSignUp ? "Sign Up" : "Sign In", { email, username, password });
      // dispatch("login");
      // Redirect to Dashboard
      isLoggedIn.set(true);
      navigate("/dashboard");
    } else {
      alert("Please provide valid credentials!");
    }
  }
  

  function toggleForm() {
    isSignUp = !isSignUp;
  }
</script>

<div class="max-w-8x2 mx-auto">
  <section id="auth" class="bg-blue-950 text-peach-cream w-full">
    <h1 class="text-4xl px-36  font-bold mb-8 ">Welcome,</h1>
    <form on:submit|preventDefault={handleSubmit} class="max-w-md mx-auto space-y-4 pb-20">
      <h2 class="text-2xl font-semibold mb-4 px-40 justify-center items-center">{isSignUp ? 'Sign Up' : 'LogIn'}</h2>
      <input type="email" bind:value={email} placeholder="Email" required class="w-full px-3 py-2 border rounded text-black" />
      {#if isSignUp}
        <input type="text" bind:value={username} placeholder="Username" required class="w-full px-3 py-2 border rounded text-black" />
      {/if}
      <input type="password" bind:value={password} placeholder="Password" required class="w-full px-3 py-2 border rounded text-black" />
      <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition-colors">
        {isSignUp ? 'Sign Up' : 'LogIn'}
      </button>
      <p class="text-center">
        {isSignUp ? 'Already have an account?' : "Don't have an account?"}
        <button type="button" on:click={toggleForm} class="text-blue-600 hover:underline ml-1">
          {isSignUp ? 'LogIn' : 'Sign Up'}
        </button>
      </p>
    </form>
  </section>

  <section id="services" class="text-blue-950 bg-peach-cream px-16 pt-20">
    <h2 class="text-3xl font-bold pl-20">What we do?</h2>
    <p class="px-24 pr-96 pb-16">
      We help students assess their academic level by conducting personalized tests. After evaluating their performance, we provide a detailed roadmap and review to highlight their strengths and areas for improvement.
      <br>
      Along with this, we offer tailored study materials to help them enhance their skills and achieve their full potential. Our goal is to guide students on their learning journey, providing the support they need to grow and succeed academically.
    </p>
  </section>

  <section id="about" class="text-blue-950 bg-peach-cream pb-16 pl-96 pr-16">
    <h2 class="text-3xl font-bold">Who are we?</h2>
    <p class="px-4">
      Hi! We're a team of six students from Usha Mittal Institute of Technology, SNDT Women's University, united by a passion for making learning simple, enjoyable, and accessible. This website is our SIH Hackathon project, designed to create a platform that empowers learners from all backgrounds.
      <br>
      Our mission is to make education fun and engaging with an intuitive, user-friendly platform. With our diverse skills in web development, design, and content creation, we're building a space that evolves with your learning needs. Join us on this exciting journey toward accessible, interactive, and enjoyable learning!
    </p>
  </section>

  <section id="contact" class="bg-blue-950 text-peach-cream px-16 pt-4">
    <h2 class="text-3xl font-bold mb-4">Contact Us!</h2>
    <div class="pl-96 space-x-10 pb-10 justify-end">
        <a href="https://www.email.com" target="_blank" class="text-white hover:text-blue-600">
            <i class="fas fa-envelope fa-2x"></i>
        </a>
        <a href="https://instagram.com" target="_blank" class="text-white hover:text-blue-400">
            <i class="fab fa-instagram fa-2x"></i>
        </a>
        <a href="https://www.linkedin.com" target="_blank" class="text-white hover:text-blue-700">
            <i class="fab fa-linkedin-in fa-2x"></i>
        </a>
    </div>
</section>

</div>

