// if there are toasts visible
// https://picturepan2.github.io/spectre/components/toasts.html
// this will make it dissapear, if the user clicks on the X
const toasts = document.querySelectorAll(".toast button");
const deleteimgbtn = document.querySelectorAll(".btn-delete-img");

toasts.forEach((el) =>
  el.addEventListener("click", (event) => {
    event.target.closest(".toast").remove();
  })
);

deleteimgbtn.forEach((el) =>
  el.addEventListener("click", (event) => {
    const teaserImageInput = document.querySelector(
      'input[name="teaser_image"]'
    );
    teaserImageInput.classList.remove("hidden");
    const container = event.target.closest(".image-container");
    const hiddenimg = document.getElementById("originalTeaserImage");
    container.remove();
    hiddenimg.remove();
  })
);
