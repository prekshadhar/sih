<script>
    let review = "You are great!";
    let roadmap = "Your personalized roadmap is ready:";
  
    function downloadRoadmap() {
      console.log("Downloading roadmap");
    }
  
    function shareRoadmap() {
      console.log("Sharing roadmap");
    }
  </script>
  
  <div class="max-w-2xl mx-auto mt-8">
    <h1 class="text-3xl font-bold mb-6">Mitra</h1>
    <div class="bg-gray-100 p-6 rounded-lg mb-6">
      <h2 class="text-2xl font-semibold mb-4">Review</h2>
      <p>{review}</p>
    </div>
    <div class="bg-gray-100 p-6 rounded-lg mb-6">
      <h2 class="text-2xl font-semibold mb-4">Roadmap</h2>
      <p>{roadmap}</p>
    </div>
    <div class="flex space-x-4">
      <button on:click={downloadRoadmap} class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors">
        Download
      </button>
      <button on:click={shareRoadmap} class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition-colors">
        Share
      </button>
    </div>
  </div>
  
  