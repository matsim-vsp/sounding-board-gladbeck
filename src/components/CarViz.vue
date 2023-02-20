<template lang="pug">
    div(id="car-viz-total")
        div(id="car-viz-left")
        div(id="car-viz-middle-1" class="car-viz-middle")
        div(id="car-viz-middle-2" class="car-viz-middle")
        div(id="car-viz-middle-3" class="car-viz-middle")
        div(id="car-viz-middle-4" class="car-viz-middle")
        div(id="car-viz-middle-5" class="car-viz-middle")
        div(id="car-viz-middle-6" class="car-viz-middle")
        div(id="car-viz-middle-7" class="car-viz-middle")
        div(id="car-viz-middle-8" class="car-viz-middle")
        div(id="car-viz-middle-9" class="car-viz-middle")
        div(id="car-viz-right")

        div(id="car-viz-middle-right")
        div(id="car-viz-middle-left")

        div(class="parking-spot parking-spot-left parking-spot-row-1")
        div(class="parking-spot parking-spot-left parking-spot-row-2")
        div(class="parking-spot parking-spot-left parking-spot-row-3")
        div(class="parking-spot parking-spot-left parking-spot-row-4")
        div(class="parking-spot parking-spot-left parking-spot-row-5")
        div(class="parking-spot parking-spot-left parking-spot-row-6")
        div(class="parking-spot parking-spot-left parking-spot-row-7")
        div(class="parking-spot parking-spot-left parking-spot-row-8")
        div(class="parking-spot parking-spot-left parking-spot-row-9")
        div(class="parking-spot parking-spot-left parking-spot-row-10")
        div(class="parking-spot parking-spot-left parking-spot-row-11")
        

        div(class="parking-spot parking-spot-right parking-spot-row-1")
        div(class="parking-spot parking-spot-right parking-spot-row-2")
        div(class="parking-spot parking-spot-right parking-spot-row-3")
        div(class="parking-spot parking-spot-right parking-spot-row-4")
        div(class="parking-spot parking-spot-right parking-spot-row-5")
        div(class="parking-spot parking-spot-right parking-spot-row-6")
        div(class="parking-spot parking-spot-right parking-spot-row-7")
        div(class="parking-spot parking-spot-right parking-spot-row-8")
        div(class="parking-spot parking-spot-right parking-spot-row-9")
        div(class="parking-spot parking-spot-right parking-spot-row-10")
        div(class="parking-spot parking-spot-right parking-spot-row-11")
        

        //- Image Source
        //- https://uxwing.com/car-top-view-icon/
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-1" class="car-viz-car car-viz-car-left car-viz-car-parking-row-1" :class="{ 'car-viz-grey': showParking(1), 'car-viz-black': !showParking(1) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-2" class="car-viz-car car-viz-car-left car-viz-car-parking-row-2" :class="{ 'car-viz-grey': showParking(5), 'car-viz-black': !showParking(5) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-3" class="car-viz-car car-viz-car-left car-viz-car-parking-row-3" :class="{ 'car-viz-grey': showParking(8), 'car-viz-black': !showParking(8) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-4" class="car-viz-car car-viz-car-left car-viz-car-parking-row-4" :class="{ 'car-viz-grey': showParking(2), 'car-viz-black': !showParking(2) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-5" class="car-viz-car car-viz-car-left car-viz-car-parking-row-5" :class="{ 'car-viz-grey': showParking(6), 'car-viz-black': !showParking(6) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-11" class="car-viz-car car-viz-car-left car-viz-car-parking-row-6" :class="{ 'car-viz-grey': showParking(1), 'car-viz-black': !showParking(1) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-12" class="car-viz-car car-viz-car-left car-viz-car-parking-row-7" :class="{ 'car-viz-grey': showParking(5), 'car-viz-black': !showParking(5) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-13" class="car-viz-car car-viz-car-left car-viz-car-parking-row-8" :class="{ 'car-viz-grey': showParking(8), 'car-viz-black': !showParking(8) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-14" class="car-viz-car car-viz-car-left car-viz-car-parking-row-9" :class="{ 'car-viz-grey': showParking(2), 'car-viz-black': !showParking(2) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-15" class="car-viz-car car-viz-car-left car-viz-car-parking-row-10" :class="{ 'car-viz-grey': showParking(6), 'car-viz-black': !showParking(6) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-6" class="car-viz-car car-viz-car-right car-viz-car-parking-row-1" :class="{ 'car-viz-grey': showParking(9), 'car-viz-black': !showParking(9) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-7" class="car-viz-car car-viz-car-right car-viz-car-parking-row-2" :class="{ 'car-viz-grey': showParking(3), 'car-viz-black': !showParking(3) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-8" class="car-viz-car car-viz-car-right car-viz-car-parking-row-3" :class="{ 'car-viz-grey': showParking(7), 'car-viz-black': !showParking(7) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-9" class="car-viz-car car-viz-car-right car-viz-car-parking-row-4" :class="{ 'car-viz-grey': showParking(10), 'car-viz-black': !showParking(10) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-10" class="car-viz-car car-viz-car-right car-viz-car-parking-row-5" :class="{ 'car-viz-grey': showParking(4), 'car-viz-black': !showParking(4) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-16" class="car-viz-car car-viz-car-right car-viz-car-parking-row-6" :class="{ 'car-viz-grey': showParking(9), 'car-viz-black': !showParking(9) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-17" class="car-viz-car car-viz-car-right car-viz-car-parking-row-7" :class="{ 'car-viz-grey': showParking(3), 'car-viz-black': !showParking(3) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-18" class="car-viz-car car-viz-car-right car-viz-car-parking-row-8" :class="{ 'car-viz-grey': showParking(7), 'car-viz-black': !showParking(7) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-19" class="car-viz-car car-viz-car-right car-viz-car-parking-row-9" :class="{ 'car-viz-grey': showParking(10), 'car-viz-black': !showParking(10) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car" id="car-viz-car-parking-10" class="car-viz-car car-viz-car-right car-viz-car-parking-row-10" :class="{ 'car-viz-grey': showParking(4), 'car-viz-black': !showParking(4) }" )

        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-1" class="car-viz-car car-viz-car-middle-left car-viz-car-row-1" :class="{ 'car-viz-grey': showDriving(4), 'car-viz-black': !showDriving(4) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-2" class="car-viz-car car-viz-car-middle-left car-viz-car-row-2" :class="{ 'car-viz-grey': showDriving(7), 'car-viz-black': !showDriving(7) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-3" class="car-viz-car car-viz-car-middle-left car-viz-car-row-3" :class="{ 'car-viz-grey': showDriving(10), 'car-viz-black': !showDriving(10) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-4" class="car-viz-car car-viz-car-middle-left car-viz-car-row-4" :class="{ 'car-viz-grey': showDriving(3), 'car-viz-black': !showDriving(3) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-5" class="car-viz-car car-viz-car-middle-left car-viz-car-row-5" :class="{ 'car-viz-grey': showDriving(6), 'car-viz-black': !showDriving(6) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-6" class="car-viz-car car-viz-car-middle-right car-viz-car-row-6" :class="{ 'car-viz-grey': showDriving(9), 'car-viz-black': !showDriving(9) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-7" class="car-viz-car car-viz-car-middle-right car-viz-car-row-7" :class="{ 'car-viz-grey': showDriving(2), 'car-viz-black': !showDriving(2) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-8" class="car-viz-car car-viz-car-middle-right car-viz-car-row-8" :class="{ 'car-viz-grey': showDriving(5), 'car-viz-black': !showDriving(5) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-9" class="car-viz-car car-viz-car-middle-right car-viz-car-row-9" :class="{ 'car-viz-grey': showDriving(8), 'car-viz-black': !showDriving(8) }" )
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car" id="car-viz-car-driving-10" class="car-viz-car car-viz-car-middle-right car-viz-car-row-10" :class="{ 'car-viz-grey': showDriving(1), 'car-viz-black': !showDriving(1) }" )
</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'

@Component({ components: {}, props: {} })
export default class VueComponent extends Vue {
  @Prop({ required: true }) private numberOfDrivingCars!: number
  @Prop({ required: true }) private numberOfParkingCars!: number
  @Prop({ required: true }) private plotWidth!: any
  @Prop({ required: true }) private plotHeight!: any

  private showParking(n: number) {
    return Math.abs(10 - this.numberOfParkingCars) > n - 1
  }

  private showDriving(n: number) {
    return Math.abs(10 - this.numberOfDrivingCars) > n - 1
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
    const width = document.getElementsByClassName('metric')[0]?.clientWidth - 30
    const factorWidth = width / carWidth

    const htmlElement = document.getElementsByClassName('car-viz-styles')[0] as HTMLElement

    if (factorHeight > factorWidth) htmlElement.style.scale = factorWidth.toString()
    else htmlElement.style.scale = factorHeight.toString()
  }

  private mounted() {}
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
