async function getLatestCo2() {
	const res = await axios.get('http://localhost:3000/LatestCo2');
	if (res && res.data && res.data.length >= 1) {
		const co2_val = res.data[0].co2_val;

		var co2Text = document.getElementById('co2-text');
		co2Text.textContent = co2_val;
	}
}

setInterval(() => {
	getLatestCo2();
}, 5000);
