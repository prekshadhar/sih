<script>
  import { onMount } from 'svelte';
  import { navigate } from 'svelte-routing';
  import { user } from '/store.js';

  let username = '';
  let emailId = '';
  let assessmentsDone = 0;

  onMount(() => {
    if ($user) {
      username = $user.username;
      emailId = $user.email;
    } else {
      navigate("/login");
    }
  });

  function handleEditProfile() {
    console.log("Edit profile clicked");
    // Implement edit profile functionality here
  }
</script>

<div class="max-w-2xl mx-auto mt-8">
  <h1 class="text-3xl font-bold mb-6">Welcome Back, {username}!</h1>
  <h2 class="text-2xl font-semibold mb-4">Profile</h2>
  <p class="mb-4">Hello {username}, This is your profile. You can see the number of assessments you have taken and can edit your profile.</p>
  <div class="bg-blue-100 p-6 rounded-lg">
    <div class="mb-4">
      <span class="font-semibold">Username:</span> {username}
    </div>
    <div class="mb-4">
      <span class="font-semibold">Email ID:</span> {emailId}
    </div>
    <div class="mb-4">
      <span class="font-semibold">Assessments Done:</span> {assessmentsDone}
    </div>
  </div>
  <button 
    class="mt-6 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors"
    on:click={handleEditProfile}
  >
    EDIT PROFILE
  </button>
</div>

