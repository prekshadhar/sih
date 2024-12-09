<script>
    let selectedBoard = "";
    let selectedStandard = "";
    let selectedSubject = "";
  
    function generateTest() {
      console.log("Generating test for:", { selectedBoard, selectedStandard, selectedSubject });
    }
  </script>
  
  <div class="max-w-2xl mx-auto mt-8">
    <h1 class="text-3xl font-bold mb-6">Assessments</h1>
    <div class="space-y-4">
      <div>
        <label for="board" class="block mb-1">Select Board</label>
        <select id="board" bind:value={selectedBoard} class="w-full px-3 py-2 border rounded">
          <option value="">Choose a board</option>
          <option value="CBSE">CBSE</option>
          <option value="ICSE">ICSE</option>
          <!-- Add more board options as needed -->
        </select>
      </div>
      <div>
        <label for="standard" class="block mb-1">Choose Standard</label>
        <select id="standard" bind:value={selectedStandard} class="w-full px-3 py-2 border rounded">
          <option value="">Choose a standard</option>
          <option value="9">9th</option>
          <option value="10">10th</option>
          <!-- Add more standard options as needed -->
        </select>
      </div>
      <div>
        <label for="subject" class="block mb-1">Select Subject</label>
        <select id="subject" bind:value={selectedSubject} class="w-full px-3 py-2 border rounded">
          <option value="">Choose a subject</option>
          <option value="Math">Math</option>
          <option value="Science">Science</option>
          <!-- Add more subject options as needed -->
        </select>
      </div>
      <button on:click={generateTest} class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition-colors">
        Generate Test
      </button>
    </div>
  </div>
  
  