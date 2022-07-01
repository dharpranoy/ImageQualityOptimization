class Slider {
  constructor (rangeElement, valueElement, options) {
    this.rangeElement = rangeElement
    this.valueElement = valueElement
    this.options = options

    this.rangeElement.addEventListener('input', this.updateSlider.bind(this))
  }

  init() {
    this.rangeElement.setAttribute('min', options.min)
    this.rangeElement.setAttribute('max', options.max)
    this.rangeElement.value = options.cur

    this.updateSlider()
  }

  asPercentage(value) {
    return parseInt(value)+'%'
      .toLocaleString('en-US', { maximumFractionDigits: 2 })
  }

  generateBackground(rangeElement) {   
    if (this.rangeElement.value === this.options.min) {
      return
    }

    let percentage =  (this.rangeElement.value - this.options.min) / (this.options.max - this.options.min) * 100
    return 'background: linear-gradient(to right, #50299c, #7a00ff ' + percentage + '%, #d3edff ' + percentage + '%, #dee1e2 100%)'
  }

  updateSlider (newValue) {
    let value = this.asPercentage(this.rangeElement.value)
    this.valueElement.innerHTML = value
    let num=parseInt(value.slice(0,-1))
    console.log(num)
    fetch('/processimg',{
		    method:'POST',
	    	body:JSON.stringify({'qua':num}),
	    	headers: {'Content-type':'application/json'}
    })
    .then(request => request.json())	
    .then(cons=>{
    	for (co of cons){
			
	    }
    })
    this.rangeElement.style = this.generateBackground(this.rangeElement.value)
  }
}

let rangeElement = document.querySelector('.range [type="range"]')
let valueElement = document.querySelector('.range .range__value span') 

let options = {
  min: 1,
  max: 100,
  cur: 80
}

if (rangeElement) {
  let slider = new Slider(rangeElement, valueElement, options)

  slider.init()
}
