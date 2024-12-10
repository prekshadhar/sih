<script>
	import { Router, Link, Route } from "svelte-routing";
	import { isLoggedIn } from "./store"; 
	import Navbar from "./components/Navbar.svelte";
	
	import Home from "./routes/Home.svelte";
	import Dashboard from "./routes/Dashboard.svelte";
	import Profile from "./routes/Profile.svelte";
	import Assessments from "./routes/Assessments.svelte";
	import Mitra from "./routes/Mitra.svelte";
	import MyLearnings from "./routes/MyLearnings.svelte";
	import Feedback from "./routes/Feedback.svelte";
  
	let url = "";
  </script>
  
  <Router {url}>
	{#if $isLoggedIn}
	  <Navbar>
		<div class="p-6">
		  <Route path="/" component={Dashboard} />
		  <Route path="/dashboard" component={Dashboard} />
		  <Route path="/profile" component={Profile} />
		  <Route path="/assessments" component={Assessments} />
		  <Route path="/mitra" component={Mitra} />
		  <Route path="/mylearnings" component={MyLearnings} />
		  <Route path="/feedback" component={Feedback} />
		</div>
	  </Navbar>
	{:else}
	  <main class="container ml-2 mr-2 w-full">
		<Route path="*" component={Home} />
	  </main>
	{/if}
  </Router>
  
  