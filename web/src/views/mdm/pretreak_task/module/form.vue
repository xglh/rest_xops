<template>
  <el-dialog :append-to-body="true" :visible="dialogFormVisable" :title="isAdd ? '新增任务' : '编辑任务'" :before-close="closeForm" width="850px">
    <el-form ref="form" :model="form" :rules="rules" size="small" label-width="80px">
      <el-row>
        <el-col :span="12">
          <el-form-item label="表名" prop="table_name">
            <el-input v-model="form.table_name" style="width: 300px;" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12">
          <el-form-item label="总数" prop="total_num">
            <el-input v-model="form.total_num" style="width: 300px;"/>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12">
          <el-form-item label="任务状态">
            <el-select v-model="form.task_status">
              <el-option label="未执行" value="-1"></el-option>
              <el-option label="执行中" value="0"></el-option>
              <el-option label="已执行" value="1"></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>
    <div slot="footer" class="dialog-footer">
      <el-button type="text" @click="closeForm">取消</el-button>
      <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
    </div>
  </el-dialog>
</template>

<script>
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
import { createTask, updateTask } from '@/api/mdm'

function getInitFormData() {
  return {
    'table_name': '',
    'total_num': '',
    'task_status': '-1'
  }
}

export default {
  props: {
    dialogFormVisable: {
      type: Boolean,
      required: true
    },
    isAdd: {
      type: Boolean,
      required: false,
      default: true
    },
    taskInfo: {
      type: Object,
      required: false,
      default: () => {
        return getInitFormData()
      }
    }
  },
  data() {
    const isNum = (rule, value, callback) => {
      const age = /^[0-9]*$/
      if (!age.test(value)) {
        callback(new Error('只能为数字'))
      } else {
        callback()
      }
    }

    return {
      loading: false,
      roleIds: [],
      form: this.taskInfo,
      rules: {
        table_name: [
          { required: true, message: '请输入表名', trigger: 'blur' },
          { min: 3, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
        ],
        task_num: [
          { validator: isNum, trigger: 'blur' }
        ]
      }
    }
  },
  watch: {
    dialogFormVisable(val) {
      this.form = this.taskInfo
    }
  },
  methods: {
    closeForm() {
      this.$emit('update:dialogFormVisable', false)
      this.resetForm()
    },
    doSubmit() {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          if (this.isAdd) {
            this.doCreate()
          } else {
            this.doUpdate()
          }
        }
      })
    },
    doUpdate() {
      const taskId = this.form.id
      const data = {
        table_name: this.form.table_name,
        total_num: this.form.total_num,
        task_status: parseInt(this.form.task_status)
      }
      this.loading = true
      updateTask(taskId, data).then(res => {
        if (res.success) {
          this.$message({
            type: 'success',
            message: '修改成功!',
            duration: 1500
          })
          this.fetchData()
        } else {
          this.$message({
            type: 'danger',
            message: '修改失败!',
            duration: 1500
          })
        }
      }).catch(err => {
        this.loading = true
        console.log(err)
      })
    },
    doCreate() {
      var form_new = Object.assign({}, this.form)
      form_new.task_status = parseInt(form_new.task_status)
      this.loading = true
      createTask(form_new).then(res => {
        if (res.success) {
          this.$message({
            type: 'success',
            message: '新增成功!',
            duration: 1500
          })
          this.fetchData()
        } else {
          this.$message({
            type: 'danger',
            message: '新增失败!',
            duration: 1500
          })
        }
      }).catch(err => {
        this.loading = true
        console.log(err)
      })
    },
    resetForm() {
      this.$refs['form'].resetFields()
      this.form = getInitFormData()
    },
    fetchData() {
      this.closeForm()
      this.loading = false
      if (this.isAdd) {
        this.$parent.$parent.init()
      } else {
        this.$parent.init()
      }
    }
  }
}

</script>

<style scoped>

</style>
