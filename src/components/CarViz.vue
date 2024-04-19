<template lang="pug">
#car-viz-total
    #car-viz-left 
    .car-viz-middle(v-for="n in 9", :key="n+'A'", :id="'car-viz-middle-' + n")
    #car-viz-right 

    #car-viz-middle-right
    #car-viz-middle-left

    div(v-for="n in 11", :key="n+'B'", :class="'parking-spot parking-spot-left parking-spot-row-' + n")
    div(v-for="n in 11", :key="n+'C'", :class="'parking-spot parking-spot-right parking-spot-row-' + n")

    //- Image Source
    //- https://uxwing.com/car-top-view-icon/

    //- parked Cars (must be incremented by 5 for each loop since class index resets after each 5) 
    img(v-for="n in 10", :key="n+'D'", :id="'car-viz-car-parking-' + n", src="../assets/images/car-top-view-icon.svg" alt="Parking Car" 
    :class="showParking(getLeftParkingStateArguments(n-1)) ? 'car-viz-car car-viz-car-left car-viz-car-parking-row-' + n + ' car-viz-grey' : 'car-viz-car car-viz-car-left car-viz-car-parking-row-' + n + ' car-viz-black'")

    img(v-for="n in 10", :key="n+'E'", :id="'car-viz-car-parking-' + (n + 10) ", src="../assets/images/car-top-view-icon.svg" alt="Parking Car" 
    :class="showParking(getRightParkingStateArguments(n-1)) ? 'car-viz-car car-viz-car-right car-viz-car-parking-row-' + n + ' car-viz-grey' : 'car-viz-car car-viz-car-right car-viz-car-parking-row-' + n + ' car-viz-black'")
    
    //- driving Cars
    img(v-for="n in 5", :key="n+'F'", :id="'car-viz-car-driving-' + n ", src="../assets/images/car-top-view-icon.svg" alt="Driving Car" 
    :class="showParking(getDrivingStateArguments(n-1)) ? 'car-viz-car car-viz-car-middle-left car-viz-car-row-' + n + ' car-viz-grey' : 'car-viz-car car-viz-car-middle-left car-viz-car-row-' + n + ' car-viz-black'")

    img(v-for="n in 5", :key="n+'G'", :id="'car-viz-car-driving-' + n ", src="../assets/images/car-top-view-icon.svg" alt="Driving Car" 
    :class="showParking(getDrivingStateArguments((n+5)-1)) ? 'car-viz-car car-viz-car-middle-right car-viz-car-row-' + (n + 5) + ' car-viz-grey' : 'car-viz-car car-viz-car-middle-right car-viz-car-row-' + (n + 5) + ' car-viz-black'")
</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'

// Diemensions:
//  Width: 150px
//  Height: 253px

const leftParkingStateArguments: number[] = [1, 5, 8, 2, 6, 1, 5, 8, 2, 6]
const rightParkingStateArguments: number[] = [9, 3, 7, 10, 4, 9, 3, 10, 7, 4]
const drivingStateArguments: number[] = [4, 7, 10, 3, 6, 9, 2, 5, 8, 1]

@Component({ components: {}, props: {} })
export default class VueComponent extends Vue {
  @Prop({ required: true }) private numberOfDrivingCars!: number
  @Prop({ required: true }) private numberOfParkingCars!: number
  @Prop({ required: true }) private plotWidth!: any
  @Prop({ required: true }) private plotHeight!: any

  private showParking(n: number) {
    if (Math.abs(10 - this.numberOfParkingCars) > n - 1) return true
    else return false
  }

  private showDriving(n: number) {
    if (Math.abs(10 - this.numberOfDrivingCars) > n - 1) return true
    else return false
  }

  private getLeftParkingStateArguments(n: number) {
    console.log(leftParkingStateArguments[n])
    return leftParkingStateArguments[n]
  }

  private getRightParkingStateArguments(n: number) {
    console.log(rightParkingStateArguments[n])
    return rightParkingStateArguments[n]
  }

  private getDrivingStateArguments(n: number) {
    return drivingStateArguments[n]
  }

  @Watch('$numberOfDrivingCars') updateNumberOfDrivingCars() {
    this.mounted()
  }

  @Watch('$numberOfParkingCars') updateNumberOfParkingCars() {
    this.mounted()
  }

  @Watch('plotWidth') updateWidth() {
    this.resizeCarViz()
  }

  @Watch('plotHeight') updateHeight() {
    this.resizeCarViz()
  }

  private resizeCarViz() {
    const carHeight = document.getElementsByClassName('car-viz-styles')[0].clientHeight
    const height = document.getElementsByClassName('metric')[0]?.clientHeight
    const factorHeight = height / carHeight
    const carWidth = document.getElementsByClassName('car-viz-styles')[0].clientWidth
    const width = document.getElementsByClassName('metric')[0]?.clientWidth
    const factorWidth = width / carWidth
    const htmlElement = document.getElementsByClassName('car-viz-styles')[0] as HTMLElement
    if (factorHeight > factorWidth) htmlElement.style.scale = (factorWidth * 0.95).toString()
    else htmlElement.style.scale = (factorHeight * 0.95).toString()
  }

  private mounted() {
    this.resizeCarViz()
  }
}
</script>

<style scoped lang="scss">
@import '@/styles.scss';

#car-viz-total {
  position: relative;
  width: 150px;
  height: 253px;
}

#car-viz-left {
  position: absolute;
  background-color: black;
  top: 0;
  bottom: 0;
  left: 0;
  width: 3px;
}

.car-viz-middle {
  position: absolute;
  background-color: black;
  left: 73px;
  width: 3px;
  height: 15px;
}

#car-viz-middle-2 {
  top: 30px;
}

#car-viz-middle-3 {
  top: 60px;
}

#car-viz-middle-4 {
  top: 90px;
}

#car-viz-middle-5 {
  top: 120px;
}

#car-viz-middle-6 {
  top: 150px;
}

#car-viz-middle-7 {
  top: 180px;
}

#car-viz-middle-8 {
  top: 210px;
}

#car-viz-middle-9 {
  top: 240px;
  height: 13px;
}

#car-viz-middle-10 {
  top: 540px;
}

#car-viz-middle-11 {
  top: 600px;
}

#car-viz-middle-right {
  position: absolute;
  right: 45px;
  width: 3px;
  top: 0;
  bottom: 0;
  background-color: black;
}

#car-viz-middle-left {
  position: absolute;
  left: 45px;
  width: 3px;
  top: 0;
  bottom: 0;
  background-color: black;
}

#car-viz-right {
  position: absolute;
  background-color: black;
  top: 0;
  bottom: 0;
  right: 0;
  width: 3px;
}

.car-viz-car {
  position: absolute;
  width: 20px;
}

.car-viz-car-left {
  left: 14px;
  -webkit-transform: rotate(270deg);
  -moz-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  -o-transform: rotate(270deg);
  transform: rotate(270deg);
}

.car-viz-car-right {
  right: 14px;
  -webkit-transform: rotate(90deg);
  -moz-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  -o-transform: rotate(90deg);
  transform: rotate(90deg);
}

.car-viz-car-middle-left {
  left: 51px;
  -webkit-transform: rotate(180deg);
  -moz-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  -o-transform: rotate(180deg);
  transform: rotate(180deg);
}

.car-viz-car-middle-right {
  right: 51px;
}

.car-viz-car-row-1 {
  top: 0px;
}

.car-viz-car-row-2 {
  top: 50px;
}

.car-viz-car-row-3 {
  top: 100px;
}

.car-viz-car-row-4 {
  top: 150px;
}

.car-viz-car-row-5 {
  top: 200px;
}

.car-viz-car-row-6 {
  top: 20px;
}

.car-viz-car-row-7 {
  top: 70px;
}

.car-viz-car-row-8 {
  top: 120px;
}

.car-viz-car-row-9 {
  top: 170px;
}

.car-viz-car-row-10 {
  top: 220px;
}

.car-viz-car-parking-row-1 {
  top: -2px;
}

.car-viz-car-parking-row-2 {
  top: 23px;
}

.car-viz-car-parking-row-3 {
  top: 48px;
}

.car-viz-car-parking-row-4 {
  top: 73px;
}

.car-viz-car-parking-row-5 {
  top: 98px;
}

.car-viz-car-parking-row-6 {
  top: 123px;
}

.car-viz-car-parking-row-7 {
  top: 148px;
}

.car-viz-car-parking-row-8 {
  top: 173px;
}

.car-viz-car-parking-row-9 {
  top: 198px;
}

.car-viz-car-parking-row-10 {
  top: 223px;
}

.parking-spot {
  position: absolute;
  width: 45px;
  height: 3px;
  background-color: black;
}

.parking-spot-right {
  right: 0px;
}

.parking-spot-row-2 {
  top: 25px;
}

.parking-spot-row-3 {
  top: 50px;
}

.parking-spot-row-4 {
  top: 75px;
}

.parking-spot-row-5 {
  top: 100px;
}

.parking-spot-row-6 {
  top: 125px;
}

.parking-spot-row-7 {
  top: 150px;
}

.parking-spot-row-8 {
  top: 175px;
}

.parking-spot-row-9 {
  top: 200px;
}

.parking-spot-row-10 {
  top: 225px;
}

.parking-spot-row-11 {
  top: 250px;
}

.parking-spot-row-12 {
  top: 275px;
}

.car-viz-grey {
  filter: invert(82%);
  transition: all 1s;
}

.car-viz-black {
  filter: invert(0%);
  transition: all 0.7s;
}
</style>
