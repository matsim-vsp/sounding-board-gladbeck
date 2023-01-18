<i18n>
en:
  results: 'Results'
  settings: 'Experiment conditions'
  title: 'Emissions Scenario Calculator'
  risk-calculator: 'Personal Risk Calculator'
  badpage: 'That page not found, sorry!'
  released: 'Released'
  estimated-risk: 'Estimated Infection Risk'
  explore-scenarios: 'Explore typical scenarios'
  try-combos: '...or try different combinations below.'
  remarks: 'Remarks'
de:
  results: 'Ergebnis'
  settings: 'Experiment conditions'
  risk-calculator: 'Personalrisiko Rechner'
  badpage: 'Seite wurde nicht gefunden.'
  released: 'Veröffentlicht'
  explore-scenarios: 'Typische Szenarien erforschen'
  try-combos: '...oder versuchen Sie verschiedene Kombinationen unten.'
  estimated-risk: 'Geschätztes Infektionsrisiko'
  remarks: 'Bemerkungen'
</i18n>

<template lang="pug">
#scenario-calculator
  //- .banner
  //-   h2 VSP / Technische Universität Berlin
  //-   h3 {{ $t('title') }}

  //- .center-area(v-if="yaml")
  .heading
    h2 {{ title }}
    p some explanatory text

  .results
    h2 {{ $t('results')  }}

    .metric(v-for="metric in metrics")
      h4.metric-title {{ metric.title  }}
      .metric-value {{ metric.value }}

  .configurator
    h2 {{ $t('settings')  }}

    .factors
      .factor(v-for="factor in Object.keys(yaml.inputColumns)")
        h4.metric-title {{ factor  }}
        .factor-option(v-for="option in factors[factor]") {{ option }}

</template>

<script lang="ts">
import { Vue, Component, Watch, Prop } from 'vue-property-decorator'
import MarkdownIt from 'markdown-it'
import Papaparse from 'papaparse'
import { Route } from 'vue-router'
import VueSlider from 'vue-slider-component'
import YAML from 'yaml'
import 'vue-slider-component/theme/default.css'

const PUBLIC_SVN = 'http://localhost:8002'
// const PUBLIC_SVN =
//   'https://svn.vsp.tu-berlin.de/repos/public-svn/matsim/scenarios/countries/de/projects/emissions-scenarios'

type ScenarioYaml = {
  data: string
  title?: string
  title_en?: string
  title_de?: string
  inputColumns: {
    [column: string]: {
      type?: string
      title?: string
      title_en?: string
      title_de?: string
    }
  }
  outputColumns: {
    [column: string]: {
      title?: string
      title_en?: string
      title_de?: string
    }
  }
  presets: any
}

@Component({ components: { VueSlider }, props: {} })
export default class VueComponent extends Vue {
  private runId = ''
  private selectedScenario = ''

  private yaml: ScenarioYaml = {
    data: '',
    title: '',
    inputColumns: {},
    outputColumns: {},
    presets: {},
  }

  private badPage = false
  private lang = 'en'
  private mdParser = new MarkdownIt()

  private sliders: { [measure: string]: { title: string; value: number } } = {}
  private lookup: { [measure: string]: { title: string; value: number }[] } = {}
  private factors: { [measure: string]: any } = {}
  private divFactors: { [measure: string]: number } = {}

  private finalR = 0
  private adjustedR = 0
  private title = ''
  private metrics: { column: string; title: string; value: any }[] = []
  private data: any[] = []

  @Watch('$route') routeChanged(to: Route, from: Route) {
    this.buildPageForURL()
  }

  private mounted() {
    this.lang = this.$i18n.locale.indexOf('de') > -1 ? 'de' : 'en'
    this.buildPageForURL()
  }

  private parseMarkdown(text: string) {
    return this.mdParser.render(text)
  }

  private async buildPageForURL() {
    this.yaml = await this.getYAML()
    this.buildUI()
    this.data = await this.loadDataset()
    this.buildOptions()
    // this.updateR()
  }

  private async getYAML() {
    this.badPage = false
    this.runId = this.$route.params.runId

    const url = `${PUBLIC_SVN}/${this.runId}/config.yaml`
    console.log({ url })

    try {
      let configText = await fetch(url).then(response => response.text())
      return YAML.parse(configText)
    } catch (e) {
      console.error('' + e)
      this.badPage = true
      return {}
    }
  }

  private buildUI() {
    this.title =
      this.lang == 'de'
        ? this.yaml.title_de || this.yaml.title || this.yaml.title_en || this.runId
        : this.yaml.title_en || this.yaml.title || this.yaml.title_de || this.runId

    // metrics
    for (const column of Object.keys(this.yaml.outputColumns)) {
      const config = this.yaml.outputColumns[column]
      const metric = {
        column,
        title:
          this.lang == 'de'
            ? config.title_de || config.title || config.title_en || column
            : config.title_en || config.title || config.title_de || column,
        value: '...',
      }
      this.metrics.push(metric)
    }
  }

  private async loadDataset() {
    const datasetFilename = `${PUBLIC_SVN}/${this.runId}/${this.yaml.data}`

    try {
      const rawData = (await fetch(datasetFilename).then(response => response.text())) as any
      const csv = Papaparse.parse(rawData, {
        header: true,
        dynamicTyping: true,
        skipEmptyLines: true,
        delimitersToGuess: ['\t', ';', ','],
      })
      console.log({ csv })
      return csv.data
    } catch (e) {
      console.log('' + e)
      return []
    }
  }

  /**
   * Discover all factor values that are in the inputColumns of the dataset
   */
  private buildOptions() {
    const inputColumns = Object.keys(this.yaml.inputColumns)

    for (const column of inputColumns) {
      this.factors[column] = new Set()
    }

    for (const row of this.data) {
      for (const column of inputColumns) {
        this.factors[column].add(row[column])
      }
    }

    this.factors = Object.assign({}, this.factors)
  }

  // private async handleDivFactorButton(measure: string) {
  //   const slider = this.sliders[measure]
  //   this.divFactors[measure] = slider.value
  //   this.updateR()
  //   this.$forceUpdate()
  // }

  // private async handleFactorButton(measure: string) {
  //   const slider = this.sliders[measure]
  //   this.factors[measure] = slider.value
  //   this.updateR()
  //   this.$forceUpdate()
  // }

  // // private async handlePreset(scenario: string) {
  // //   this.selectedScenario = this.yaml.scenarios[scenario]
  // //   for (const measure of Object.keys(this.selectedScenario.presets) as any) {
  // //     const title = this.selectedScenario.presets[measure]

  // //     //@ts-ignore:
  // //     const value = this.lookup[measure].find((a: any) => a.title === title).value

  // //     console.log(measure, title, value)

  // //     if (this.multipliers.indexOf(measure) > -1) this.factors[measure] = value
  // //     if (this.divisors.indexOf(measure) > -1) this.divFactors[measure] = value

  // //     // find this entry for the slider!
  // //     for (const choice of this.lookup[measure]) {
  // //       if (choice.title === title) {
  // //         this.sliders[measure] = choice
  // //         break
  // //       }
  // //     }
  // //   }

  //   this.updateR()
  //   this.$forceUpdate()
  // }

  // private get multipliers() {
  //   return Object.keys(this.yaml.multipliers)
  // }

  // private get divisors() {
  //   return Object.keys(this.yaml.divisors)
  // }

  // private updateR() {
  //   let r = this.yaml.calibrationParam

  //   // multiplicative factors
  //   for (const factor of Object.values(this.factors)) r *= factor
  //   // divisors factors, already 1/x
  //   for (const factor of Object.values(this.divFactors)) r *= factor
  //   // exp result
  //   r = 1.0 - Math.exp(-1.0 * r)

  //   // fancy!
  //   this.finalR = Math.min(99, r * 100.0) // percentage
  //   this.animateTowardNewRValue()
  // }

  private animateTowardNewRValue() {
    const diff = this.finalR - this.adjustedR
    const step = this.adjustedR + diff * 0.2
    this.adjustedR = step

    if (Math.abs(this.adjustedR - this.finalR) < 0.01) {
      this.adjustedR = this.finalR
    } else {
      setTimeout(this.animateTowardNewRValue, 16)
    }
  }

  // private buildUI() {
  // // multiplicative factors
  // for (const measureName of Object.keys(this.yaml.multipliers)) {
  //   const measures = this.yaml.multipliers[measureName]
  //   this.lookup[measureName] = []
  //   for (const option of measures.options) {
  //     const title = Object.keys(option)[0]
  //     const value = option[title]
  //     if (!isNaN(value)) {
  //       this.lookup[measureName].push({ title, value })
  //       // first?
  //       if (this.yaml.multipliers[measureName].options === undefined) {
  //         this.factors[measureName] = value
  //         this.sliders[measureName] = this.lookup[measureName][0]
  //       }
  //     } else {
  //       // user specified a default with an asterisk* after the number
  //       const trimAsterisk = parseFloat(value.substring(0, value.length - 1))
  //       const choice = { title, value: trimAsterisk }
  //       this.lookup[measureName].push(choice)
  //       this.sliders[measureName] = choice
  //       this.factors[measureName] = trimAsterisk
  //     }
  //   }
  // }
  // // divisors
  // for (const measureName of Object.keys(this.yaml.divisors)) {
  //   const measures = this.yaml.divisors[measureName]
  //   this.lookup[measureName] = []
  //   for (const option of measures.options) {
  //     const title = Object.keys(option)[0]
  //     const value = option[title]
  //     if (!isNaN(value)) {
  //       this.lookup[measureName].push({ title, value: 1.0 / value })
  //       // first?
  //       if (this.yaml.divisors[measureName].options === undefined) {
  //         this.divFactors[measureName] = value
  //         this.sliders[measureName] = this.lookup[measureName][0]
  //       }
  //     } else {
  //       // user specified a default with an asterisk* after the number
  //       const trimAsterisk = 1.0 / parseFloat(value.substring(0, value.length - 1))
  //       const choice = { title, value: trimAsterisk }
  //       this.lookup[measureName].push(choice)
  //       this.sliders[measureName] = choice
  //       this.divFactors[measureName] = trimAsterisk
  //     }
  //   }
  // }
  // }
}
</script>

<style scoped lang="scss">
@import '@/styles.scss';

#scenario-calculator {
  background-color: #224;
  color: #eee;
}
.center-area {
  max-width: 70rem;
  padding: 1rem 3rem 1rem 3rem;
}

.option-groups {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.option-group {
  border: solid 1px #bbf;
  border-radius: 4px;
  background-color: #fff;
  padding: 0.5rem 0.5rem;
}

.measures {
  padding: 0.5rem 0;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

h2 {
  font-size: 2rem;
  text-transform: uppercase;
}

h3 {
  font-weight: normal;
  font-size: 1.3rem;
  margin-bottom: -0.5rem;
}

h4 {
  color: #596;
  font-size: 1.2rem;
  font-weight: bold;
  margin: 0 0 0 0;
  padding: 0 0;
}

.button {
  padding: 0 0.5rem;
  margin: 0 0.15rem 0.15rem 0;
}

p {
  margin-bottom: 1rem;
}

p.factor {
  margin: auto 0 auto 1rem;
  color: #ccc;
}

.banner {
  display: flex;
  flex-direction: column;
  padding: 4rem 3rem 1rem 3rem;
  background-color: #1e1f2c;
  color: white;
  background: url(../assets/images/banner.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}

.banner h2 {
  margin-bottom: 0rem;
  font-size: 1.6rem;
  background-color: #1e1f2c;
  line-height: 1.6rem;
  margin-right: auto;
}

.banner h3 {
  font-size: 1.3rem;
  font-weight: normal;
  margin-bottom: 0;
  line-height: 1.4rem;
  padding-bottom: 0.25rem;
  background-color: #1e1f2c;
  width: max-content;
}

.base-buttons {
  margin-bottom: 1rem;
}

.greenbig {
  color: #596;
  font-weight: bold;
  font-size: 2.5rem;
}

.notes-item {
  list-style-type: square;
  margin-left: 1rem;
  margin-top: 0.5rem;
  color: #222;
}

li.notes-item {
  line-height: 1.3rem;
}

.description {
  font-size: 0.85rem;
  margin-top: 0;
  margin-bottom: 0.25rem;
}

.sticky {
  top: 3rem;
  position: sticky;
  background-color: #eee;
  padding-top: 0;
  padding-bottom: 0rem;
}

.slider {
  margin: 0.5rem 0.5rem;
}

.slider-label {
  font-size: 0.9rem;
  font-weight: bold;
  color: #383ab1;
  margin: 0 0;
}

.results {
  background-color: #154b30;
  padding: 1rem 2rem 2rem 2rem;
}

.configurator {
  background-color: #441b5d;
  padding: 1rem 2rem 2rem 2rem;
}

.metric {
  background-color: white;
  width: max-content;
  padding: 1rem;
}

.metric-value {
  font-weight: bold;
  font-size: 2rem;
  color: #222;
}

.heading {
  padding: 2rem;
}

.factors {
  display: flex;
}

.factor {
  padding: 1rem;
  background-color: white;
  margin: 0.5rem;
}

.factor-option {
  color: #227;
  background-color: #cc3;
  margin: 0.25rem;
  cursor: pointer;
}

@media only screen and (max-width: 850px) {
  .option-groups {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media only screen and (max-width: 640px) {
  .banner {
    padding: 2rem 1rem;
  }

  .center-area {
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .option-groups {
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>
