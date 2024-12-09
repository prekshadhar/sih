<script>
    let userId = "12345";
    let emailId = "user@example.com";
    let board = "CBSE";
    let standard = "10th";
    let assessmentsDone = 5;
  </script>
  
  <div class="max-w-2xl mx-auto mt-8">
    <h1 class="text-3xl font-bold mb-6">Welcome Back!</h1>
    <h2 class="text-2xl font-semibold mb-4">Profile</h2>
    <p class="mb-4">Hello User, This is your profile you can see the number of assessments you have taken and can edit your profile.</p>
    <div class="bg-gray-100 p-6 rounded-lg">
      <div class="mb-4">
        <span class="font-semibold">User ID:</span> {userId}
      </div>
      <div class="mb-4">
        <span class="font-semibold">Email ID:</span> {emailId}
      </div>
      <div class="mb-4">
        <span class="font-semibold">Board:</span> {board}
      </div>
      <div class="mb-4">
        <span class="font-semibold">Standard:</span> {standard}
      </div>
      <div class="mb-4">
        <span class="font-semibold">Assessments Done:</span> {assessmentsDone}
      </div>
    </div>
    <button class="mt-6 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors">
      EDIT PROFILE
    </button>
  </div>
  
  