<template lang="pug">
vue-plotly(class="bar-plot"
  :data="data"
  :layout="layout"
  :options="options"
)
</template>

<script lang="ts">
import VuePlotly from '@twelve-co/vue-plotly'

export default {
  components: { VuePlotly },
  props: {
    data: Array,
  },

  data: () => {
    return {
      layout: {
        width: 270,
        height: 250,
        barmode: 'relative',
        autosize: true,
        showlegend: false,
        // font: {
        //   family: 'Roboto,Arial,Helvetica,sans-serif',
        //   size: 12,
        //   color: '#000',
        // },
        margin: { t: 25, r: 25, b: 25, l: 60 },
        xaxis: {
          //fixedrange: window.innerWidth < 700,
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
          range: [0.0, 1.05],
          tickformat: ',.0%',
          title: {
            text: '% Diff',
            standoff: 500,
          },
        } as any,
        plot_bgcolor: '#ffffff',
        paper_bgcolor: '#ffffff',
      },
      options: {
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
      },
    }
  },
}
</script>

<style scoped lang="scss">
@import '@/styles.scss';

@media only screen and (max-width: 640px) {
}
</style>
