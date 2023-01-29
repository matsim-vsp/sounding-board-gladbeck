<template lang="pug">
vue-plotly(
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
        width: 160,
        height: 160,
        barmode: 'relative',
        autosize: true,
        showlegend: false,
        // font: {
        //   family: 'Roboto,Arial,Helvetica,sans-serif',
        //   size: 12,
        //   color: '#000',
        // },
        margin: { t: 25, r: 25, b: 25, l: 25 },
        xaxis: {
          //fixedrange: window.innerWidth < 700,
        },
        yaxis: {
          // note this gets overwritten when the scale changes - see updateScale()
          //fixedrange: window.innerWidth < 700,
          fixedrange: true,
          range: [-1.0, 0.2],
          title: '% Diff',
        } as any,
        plot_bgcolor: '#f8f8f8',
        paper_bgcolor: '#f8f8f8',
      },
      options: {},
    }
  },
}
</script>

<style scoped lang="scss">
@import '@/styles.scss';

@media only screen and (max-width: 640px) {
}
</style>
