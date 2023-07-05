const comicContainer = document.getElementById("comic-container");
const prevBtn = document.getElementById("prev-btn");
const nextBtn = document.getElementById("next-btn");

function fetchComic(url) {
    fetch("http://127.0.0.1:8000" + url)
        .then(response => response.json())
        .then(comic => {
            comicContainer.innerHTML = `
                <h1>${comic.title}</h1>
                <img src="${comic.img}" alt="${comic.alt}">
            `;
        });
}

prevBtn.addEventListener("click", () => fetchComic("/api/get_previous_comic"));
nextBtn.addEventListener("click", () => fetchComic("/api/get_next_comic"));

fetchComic("http://127.0.0.1:8000/api/get_random_comic");
