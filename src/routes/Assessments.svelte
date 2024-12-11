<script>
  let selectedField = "";
  let selectedInterest = "";
  let selectedSubject = "";

  function generateTest() {
    console.log("Generating test for:", { selectedField, selectedInterest, selectedSubject });
  }
</script>

<div class="max-w-2xl mx-auto mt-8">
  <h1 class="text-4xl font-bold mb-8 text-left">Assessments</h1>
  <div class="flex justify-between w-full">
      <!-- Field Section with Blue Background and Larger Content -->
      <div class="bg-blue-200 p-8 rounded-lg w-[48%]">
          <div>
              <label for="field" class="block mb-2 text-lg font-semibold">Choose Field</label>
              <select id="field" bind:value={selectedField} class="w-full px-4 py-3 border rounded-lg text-lg">
                  <option value="">Choose a field</option>
                  <option value="Science">Science</option>
                  <option value="Commerce">Commerce</option>
                  <option value="Arts">Arts</option>
                  <!-- Add more field options as needed -->
              </select>
          </div>
          <button on:click={generateTest} class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition-colors mt-6 text-lg">
              Generate Test
          </button>
      </div>

      <!-- Interest Section with Blue Background and Larger Content -->
      <div class="bg-blue-200 p-8 rounded-lg w-[48%]">
          <div>
              <label for="interest" class="block mb-2 text-lg font-semibold">Choose Interest</label>
              <select id="interest" bind:value={selectedInterest} class="w-full px-4 py-3 border rounded-lg text-lg">
                  <option value="">Choose an interest</option>
                  <option value="Mathematics">Mathematics</option>
                  <option value="Physics">Physics</option>
                  <option value="Literature">Literature</option>
                  <!-- Add more interest options as needed -->
              </select>
          </div>
          <button on:click={generateTest} class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition-colors mt-6 text-lg">
              Generate Test
          </button>
      </div>
  </div>
</div>
