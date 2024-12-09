<script>
    let tests = [
      { id: 1, name: "Test 1" },
      { id: 2, name: "Test 2" },
    ];
  
    function viewReview(testId) {
      console.log("Viewing review for test:", testId);
    }
  
    function shareRoadmap(testId) {
      console.log("Sharing roadmap for test:", testId);
    }
  </script>
  
  <div class="max-w-2xl mx-auto mt-8">
    <h1 class="text-3xl font-bold mb-6">My Learnings</h1>
    <div class="space-y-6">
      {#each tests as test}
        <div class="bg-gray-100 p-6 rounded-lg">
          <h2 class="text-2xl font-semibold mb-4">{test.name}</h2>
          <div class="flex space-x-4">
            <button on:click={() => viewReview(test.id)} class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors">
              Review
            </button>
            <button on:click={() => shareRoadmap(test.id)} class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition-colors">
              Share Roadmap
            </button>
          </div>
        </div>
      {/each}
    </div>
  </div>
  
  