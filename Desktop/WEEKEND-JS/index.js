const form = document.querySelector('.search-form')
const input = document.querySelector('.search-input')
const container= document.querySelector('.container')
let userInput= ''

form.addEventListener('submit', (e) => {
    container.innerHTML=''
    e.preventDefault()
    userInput= input.value
    fetchData()
    

})



const fetchData = async() => { 
const url = 'https://ginger4.p.rapidapi.com/correction?lang=US&generateRecommendations=false&flagInfomralLanguage=true';
const options = {
	method: 'POST',
	headers: {
		'content-type': 'text/plain',
		'Content-Type': 'text/plain',
		'Accept-Encoding': 'identity',
		'X-RapidAPI-Key': '12e91dd645msh11887abd2554d28p13b1c4jsn09394f8547e0',
		'X-RapidAPI-Host': 'ginger4.p.rapidapi.com'
	},
	body: '"bonjour"'
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}


const card = document.createElement('div')
card.classList.add('card')
card.innerHTML = `

<div class = "container" > <h1>${card.corrections[0]}</h2>
`

container.appendChild(card)
}

fetchData()