<template lang="pug">
vue-plotly(class="bar-plot"
  :data="data"
  :layout="layout"
  :options="options"
  :config="config"
)
</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'
import VuePlotly from '@twelve-co/vue-plotly'
import { debounce } from 'debounce'

@Component({ components: { VuePlotly }, props: {} })
export default class VueComponent extends Vue {
  @Prop({ required: false }) private data!: any[]
  @Prop({ required: true }) private plotWidth!: any
  @Prop({ required: true }) private plotHeight!: any
  private mounted() {}

  @Watch('plotWidth') private updateWidth() {
    this.resizePlot()
  }

  @Watch('plotHeight') private updateHeight() {
    this.resizePlot()
  }

  private resizePlot() {
    if (window.innerWidth <= 1024) {
      this.layout.margin = { t: 10, r: 0, b: 10, l: 30 }
      this.layout.yaxis.tickvals = [0, 0.25, 0.5, 0.75, 1]
      this.layout.font.size = 10
      this.layout.yaxis.gridwidth = 2
      this.layout.xaxis.linewidth = 2
    } else if (window.innerWidth <= 1260) {
      this.layout.margin = { t: 10, r: 10, b: 10, l: 30 }
      this.layout.yaxis.tickvals = [0, 0.2, 0.4, 0.6, 0.8, 1]
      this.layout.font.size = 10
      this.layout.yaxis.gridwidth = 2
      this.layout.xaxis.linewidth = 2
    } else if (window.innerWidth <= 1440) {
      this.layout.margin = { t: 10, r: 10, b: 10, l: 30 }
      this.layout.yaxis.tickvals = [0, 0.2, 0.4, 0.6, 0.8, 1]
      this.layout.font.size = 10
      this.layout.yaxis.gridwidth = 1
      this.layout.xaxis.linewidth = 1
    } else {
      //   this.layout.margin = { t: 25, r: 25, b: 25, l: 50 }
      this.layout.yaxis.tickvals = [0, 0.2, 0.4, 0.6, 0.8, 1]
      this.layout.font.size = 13
      this.layout.yaxis.gridwidth = 1
      this.layout.xaxis.linewidth = 1
    }
  }

  private config: any = { responsive: true }

  private layout: any = {
    // width: 249,
    // height: 279,
    barmode: 'relative',
    autosize: true,
    showlegend: false,
    // font: {
    //   family: 'Roboto,Arial,Helvetica,sans-serif',
    //   size: 12,
    //   color: '#000',
    // },
    margin: { t: 10, r: 0, b: 10, l: 38 },
    xaxis: {
      //fixedrange: window.innerWidth < 700,
      linecolor: '#000000',
    },
    font: {
      size: 13,
      color: '#000000',
    },
    yaxis: {
      // note this gets overwritten when the scale changes - see updateScale()
      //fixedrange: window.innerWidth < 700,
      showgrid: true,
      gridwidth: 1,
      gridcolor: '#000000',
      fixedrange: true,
      range: [0, 1.05],
      tickformat: ',.0%',
      //tickvals: [0, 0.2, 0.4, 0.6, 0.8, 1],
      title: {
        //text: '% Diff',
        standoff: 500,
      },
    } as any,
    plot_bgcolor: '#ffffff',
    paper_bgcolor: '#ffffff',
  }
  private options = {
    displayModeBar: false,
    displaylogo: false,
    responsive: true,
    modeBarButtonsToRemove: [
      'pan2d',
      'zoom2d',
      'select2d',
      'lasso2d',
      'zoomIn2d',
      'zoomOut2d',
      'autoScale2d',
      'hoverClosestCartesian',
      'hoverCompareCartesian',
      'resetScale2d',
      'toggleSpikelines',
      'resetViewMapbox',
    ],
    toImageButtonOptions: {
      format: 'svg', // one of png, svg, jpeg, webp
      filename: 'daily-cases',
      width: 1200,
      height: 600,
      scale: 1.0, // Multiply title/legend/axis/canvas sizes by this factor
    },
  }
}
</script>

<style scoped lang="scss">
@import '@/styles.scss';
</style>
