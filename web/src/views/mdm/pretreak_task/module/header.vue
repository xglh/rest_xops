<template>
  <div class="head-container">
    <!-- 搜索 -->
    <el-input v-model="query.value" clearable placeholder="输入名称搜索" style="width: 200px;" class="filter-item" @keyup.enter.native="toQuery"/>
    <el-button class="filter-item" size="mini" type="primary" icon="el-icon-search" @click="toQuery">搜索</el-button>
    <!-- 新增 -->
    <div style="display: inline-block;margin: 0px 2px;">
      <el-button
        v-if="checkPermission(['admin','pretreat_task_all','pretreat_task_create'])"
        class="filter-item"
        size="mini"
        type="primary"
        icon="el-icon-plus"
        @click="dialogFormVisable=true">新增</el-button>
      <e-form :dialog-form-visable.sync="dialogFormVisable" :is-add="isAdd"></e-form>
    </div>
    <el-button
      v-if="checkPermission(['admin','pretreat_task_all','pretreat_task_delete'])"
      :loading="delLoading"
      class="filter-item"
      type="danger"
      size="mini"
      icon="el-icon-delete"
      @click="handleDeleteTasks"
    >批量删除
    </el-button>
  </div>
</template>

<script>
import checkPermission from '@/utils/permission'
import eForm from './form'
import { deleteTasks } from '@/api/mdm'
export default {
  components: { eForm },
  props: {
    query: {
      type: Object,
      required: true
    },
    deleteTaskList: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      dialogFormVisable: false,
      isAdd: true,
      delLoading: false
    }
  },
  methods: {
    checkPermission,
    toQuery() {
      this.$parent.page = 1
      this.$parent.init()
    },
    handleDeleteTasks() {
      var deleteTaskIdList = []
      this.deleteTaskList.forEach(data => {
        deleteTaskIdList.push(data.id)
      })
      if (deleteTaskIdList.length === 0) {
        this.$message({
          showClose: true,
          message: '请至少选中一条记录',
          duration: 1500,
          type: 'warning'
        })
      } else {
        this.$confirm('确认删除选中记录?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.delLoading = true
          deleteTasks(deleteTaskIdList).then(
            res => {
              console.log(res)
              if (res.success) {
                this.$message({
                  type: 'success',
                  message: '删除成功!',
                  duration: 1500
                })
                this.toQuery()
              } else {
                this.$message({
                  type: 'danger',
                  message: '删除失败!',
                  duration: 1500
                })
              }
              this.delLoading = false
            }
          )
        }).catch(err => {
          this.delLoading = false
          console.log(err)
        })
      }
    }
  }
}
</script>

<style scoped>

</style>
