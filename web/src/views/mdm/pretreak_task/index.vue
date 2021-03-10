<template>
  <div class="app-container">
    <eHeader :query="query" :delete-task-list="deleteTaskList"/>
    <el-table v-loading="loading" :data="data" size="small" border style="width: 100%;" @selection-change="handleSelectionChange">
      <el-table-column
        type="selection"
        width="40"
      />
      <el-table-column type="index" label="编号" width="100" align="center"/>
      <el-table-column prop="table_name" label="表名" width="200"/>
      <el-table-column prop="total_num" label="总数" width="200"/>
      <el-table-column label="状态" width="200">
        <template slot-scope="{row}">
          <span v-if="row.task_status===-1">未执行</span>
          <span v-if="row.task_status===0">执行中</span>
          <span v-if="row.task_status===1">执行完毕</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" align="center">
        <template slot-scope="{row}">
          <el-button slot="reference" type="primary" size="mini" style="margin: 0px 8px" @click="subEdit(row)">编辑</el-button>
          <el-popover
            v-if="checkPermission(['admin','pretreat_task_all','pretreat_task_delete'])"
            :ref="row.id"
            placement="top"
            width="180">
            <p>确定删除本条数据吗？所有关联的数据将会被清除</p>
            <div style="text-align: right; margin: 0">
              <el-button size="mini" type="text" @click="$refs[row.id].doClose()">取消</el-button>
              <el-button :loading="delLoading" type="primary" size="mini" @click="subDelete(row.id)">确定</el-button>
            </div>
            <el-button slot="reference" type="danger" size="mini">删除</el-button>
          </el-popover>
        </template>
      </el-table-column>
    </el-table>
    <eForm :dialog-form-visable.sync="dialogFormVisable" :is-add="isAdd" :task-info="taskInfo" ></eForm>
    <el-pagination
      :total="total"
      :page-sizes="[10, 20, 30, 40]"
      style="margin-top: 8px;"
      layout="total, prev, pager, next, sizes"
      @size-change="sizeChange"
      @current-change="pageChange"/>
  </div>
</template>

<script>
import initData from '@/mixins/initData'
import eHeader from './module/header'
import checkPermission from '@/utils/permission'
import eForm from './module/form'
import { deleteTask } from '@/api/mdm'
export default {
  components: { eHeader, eForm },
  mixins: [initData],
  data() {
    return {
      dialogFormVisable: false,
      isAdd: false,
      taskInfo: {},
      delLoading: false,
      deleteTaskList: []
    }
  },
  created() {
    this.$nextTick(() => {
      this.init(
        this.size = 20
      )
    })
  },
  methods: {
    checkPermission,
    beforeInit() {
      this.url = 'api/pretreat_tasks/'
      const sort = '-id'
      const query = this.query
      const value = query.value
      this.params = { page: this.page, size: this.size, ordering: sort }
      if (value) { this.params['search'] = value }
      return true
    },
    subDelete(taskId) {
      this.delLoading = true
      deleteTask(taskId).then(res => {
        if (res.success) {
          this.$message({
            showClose: true,
            type: 'success',
            message: '删除成功!',
            duration: 2500
          })
        } else {
          this.$message({
            showClose: true,
            type: 'danger',
            message: '删除失败!',
            duration: 2500
          })
        }
        this.delLoading = false
        this.$refs[taskId].doClose()
        this.init()
      }).catch(err => {
        this.delLoading = false
        console.log(err)
      })
    },
    subEdit(row) {
      this.taskInfo = Object.assign({}, row)
      this.taskInfo.task_status = String(this.taskInfo.task_status)
      this.dialogFormVisable = true
    },
    handleSelectionChange(val) {
      this.deleteTaskList = val
    }

  }
}
</script>

<style scoped>

</style>
