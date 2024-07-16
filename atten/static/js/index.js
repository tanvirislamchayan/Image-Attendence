window.addEventListener('scroll', () => {
    let navbar = this.document.querySelector('.navbar');
    navbar.classList.toggle('sticky', window.scrollY > 0);
});

const bar = document.getElementById('bar');
const navItem =  document.getElementById('nav-item');
const cls = document.getElementById('xmark');

if (bar) {
    bar.addEventListener('click', () => {
        navItem.classList.add('show');
    })
}

if (cls) {
    cls.addEventListener('click', () => {
        navItem.classList.remove('show');
    })
}

const leftBar = document.getElementById('left-bar');
const leftInnerMenu = document.getElementById('left-inner-menu');
const leftCls = document.getElementById('left-xmark');

if (leftBar) {
    leftBar.addEventListener('click', () => {
        leftInnerMenu.classList.add('show-left');
    });
}

if (leftCls) {
    leftCls.addEventListener('click', () => {
        leftInnerMenu.classList.remove('show-left');
    });
}

// load date
document.querySelectorAll('.date-field').forEach(function(field) {
    field.addEventListener('click', function() {
        document.getElementById('date').value = this.getAttribute('data-date');
    });
});

// function createDateRange(startDate, endDate) {
//     const dates = [];
//     let currentDate = new Date(startDate);

//     while (currentDate <= endDate) {
//         dates.push(new Date(currentDate));
//         currentDate.setDate(currentDate.getDate() + 1);
//     }

//     return dates;
// }

var addBtn = document.getElementById('add-btn');
var addSection = document.getElementById('add-section');
var cancelBtn = document.getElementById('cancel-btn');

if (addBtn) {
    addBtn.addEventListener('click', ()=> {
        addSection.classList.add('add-section-show');
    });
}

if (cancelBtn) {
    cancelBtn.addEventListener('click', ()=> {
        addSection.classList.remove('add-section-show');
    });
}

// image preview

document.querySelectorAll('.fileInput').forEach(input => {
    input.addEventListener('change', function(event) {
        var file = event.target.files[0];
        if (file) {
            var reader = new FileReader();
            reader.onload = function(e) {
                // Find the closest img element with the class 'preview'
                var previewImg = event.target.closest('.department_img').querySelector('.preview');
                previewImg.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});
