<template>
  <div class="app-container">
    <eHeader :dicts="dicts" :query="query"/>

    <el-pagination
      :total="total"
      :page-sizes="[100, 200, 300, 400]"
      style="margin-top: 8px;"
      layout="total, prev, pager, next, sizes"
      @size-change="sizeChange"
      @current-change="pageChange"/>
  </div>
</template>

<script>
import initData from '@/minins/data'
import eHeader from './module/header'

export default {
  components: { eHeader },
  mixins: [initData],
  data() {
    return {}
  },
  methods: {
    beforeInit() {
      this.url = 'api/pretreat_tasks/'
      const sort = 'id'
      const query = this.query
      const value = query.value
      this.params = { page: this.page, size: this.size, ordering: sort }
      if (value) { this.params['search'] = value }
      return true
    }
  }
}
</script>

<style scoped>

</style>
