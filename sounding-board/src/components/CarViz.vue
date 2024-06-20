<template lang="pug">
#car-viz-total
  .row(v-for="n in 10" :id="'row-' + n" :key="n")
    .column(style="width: 30%")
      .car-parked-left(id="parked-column")
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car"
        :class="showParking(getLeftParkingStateArguments(n-1)) ? 'car-parked-left ' + 'grey' : 'car-parked-left ' + 'black'")
    .column(style="width: 20%")
      .car-driving-left(id="driving-column" v-if="n % 2 == 1")
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car"
        :class="showDriving(getDrivingStateArguments(n-1)) ? 'car-driving-left ' + 'grey' : 'car-driving-left ' + 'black'")
    .middle-lines
    .column(style="width: 20%")
      .car-driving-right(id="driving-column" v-if="n % 2 == 0")
        img(src="../assets/images/car-top-view-icon.svg" alt="Driving Car"
        :class="showDriving(getDrivingStateArguments(n - 1)) ? 'car-driving-right ' + 'grey' : 'car-driving-right ' + 'black'")
    .column(style="width: 30%")
      .car-parked-right(id="parked-column")
        img(src="../assets/images/car-top-view-icon.svg" alt="Parking Car"
        :class="showParking(getRightParkingStateArguments(n-1)) ? 'car-parked-right ' + 'grey' : 'car-parked-right ' + 'black'")

</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'

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
    return Math.abs(10 - this.numberOfParkingCars) > n - 1
  }

  private showDriving(n: number) {
    return Math.abs(10 - this.numberOfDrivingCars) > n - 1
  }

  private getLeftParkingStateArguments(n: number) {
    return leftParkingStateArguments[n]
  }

  private getRightParkingStateArguments(n: number) {
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
  height: 100%;
  max-height: 500px;
  width: 100%;
  position: relative;
}
.row {
  display: -webkit-box;
  height: 10%;
  flex-direction: row;
  position: relative;
}

#row-10 > .column {
  height: 108%;
}

.column {
  padding: 0px;
}

.grey {
  filter: invert(82%);
  transition: all 1s;
}

.black {
  filter: invert(0%);
  transition: all 0.7s;
}

.middle-lines {
  height: 23px;
  width: 4px;
  background-color: #000;
  display: flex;
  margin-top: 5px;
}

.car-parked-left {
  height: 100%;
}

.car-parked-right {
  height: 100%;
}

.car-parked-left img {
  width: 46px;
  height: 150%;
  transform: rotate(-90deg);
  display: block;
  margin: -14px auto auto auto;
}

.car-parked-right img {
  width: 46px;
  height: 150%;
  transform: rotate(90deg);
  display: block;
  margin: -14px auto auto auto;
}

.car-driving-left {
  margin-left: 5px;
  width: 46px;
  height: 100%;
}

.car-driving-right {
  margin-left: 5px;
  width: 46px;
  height: 100%;
}

.car-driving-left img {
  height: 140%;
  transform: rotate(180deg);
  display: block;
  margin: auto;
}

.car-driving-right img {
  height: 140%;
  display: block;
  margin: auto;
}

.column > #parked-column {
  display: flex;
  border-right: 4px solid #000;
  border-left: 4px solid #000;
  border-top: 4px solid #000;
}

#row-10 > .column > #parked-column {
  border-bottom: 4px solid #000;
}
</style>
