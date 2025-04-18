<template>
  <v-app>
    <v-main class="grey lighten-5">
      <v-container>
        <v-app-bar color="white" flat class="mb-4">
          <v-toolbar-title>
            <a href="{% url 'task_list' %}" class="text-decoration-none black--text">ToDoList</a>
          </v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn text href="{% url 'task_list' %}" color="black">
            Задачи
          </v-btn>
          <v-btn text href="{% url 'task_create' %}" color="black">
            Добавить задачу
          </v-btn>
        </v-app-bar>

        <slot name="messages"></slot>
        <slot></slot>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
.v-application {
  background-color: #f5f5f5 !important;
}

.task-completed {
  text-decoration: line-through;
  color: rgba(0, 0, 0, 0.6);
}

.v-text-field.dense {
  margin-top: 0;
  padding-top: 0;
}

.v-text-field.dense .v-input__control {
  min-height: 40px;
}

.v-form {
  max-width: 600px;
  margin: 0 auto;
}

.task-card {
  transition: transform 0.2s;
}

.task-card:hover {
  transform: translateY(-2px);
}

.priority-high {
  border-left: 4px solid #ff5252;
}

.priority-medium {
  border-left: 4px solid #ffd740;
}

.priority-low {
  border-left: 4px solid #69f0ae;
}
</style> 