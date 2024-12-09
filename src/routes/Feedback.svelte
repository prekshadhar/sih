<script>
    let feedback = "";
  
    function submitFeedback() {
      console.log("Submitting feedback:", feedback);
      // Here you would typically send the feedback to your server
      feedback = ""; // Clear the feedback after submission
    }
  </script>
  
  <div class="max-w-2xl mx-auto mt-8">
    <h1 class="text-3xl font-bold mb-6">Feedback</h1>
    <p class="mb-4">Your feedback matters!</p>
    <form on:submit|preventDefault={submitFeedback} class="space-y-4">
      <div>
        <label for="feedback" class="block mb-1">Write about your experience</label>
        <textarea
          id="feedback"
          bind:value={feedback}
          rows="5"
          class="w-full px-3 py-2 border rounded"
          placeholder="Enter your feedback here"
        ></textarea>
      </div>
      <button type="submit" class="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition-colors">
        Submit
      </button>
    </form>
  </div>
  
  