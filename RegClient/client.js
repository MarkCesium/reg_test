url = 'http://127.0.0.1:5000';


fetch(
	url + "/registration",
	{
		method: 'post',
		body: JSON.stringify([{
			"username": "antony1998",
			"name": "Anton",
			"email": "AntonPupkin/gmail.com",
			"age": 25
		}]),
		headers: {
			'content-type': 'application/json'
		}
	}
).then((response) => {
	return response.json();
})
	.then((data) => {
		console.log(data);
	});