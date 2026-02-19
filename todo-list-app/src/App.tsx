import { useTodos } from './hooks/useTodos';
import { TodoInput } from './components/TodoInput';
import { TodoList } from './components/TodoList';
import { TodoFilter } from './components/TodoFilter';
import { TodoStats } from './components/TodoStats';
import { CheckSquare } from 'lucide-react';

function App() {
  const {
    filteredTodos,
    filter,
    stats,
    addTodo,
    toggleTodo,
    deleteTodo,
    clearCompleted,
    setFilter,
  } = useTodos();

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8 px-4">
      <div className="max-w-2xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-blue-500 rounded-2xl mb-4 shadow-lg">
            <CheckSquare size={32} className="text-white" />
          </div>
          <h1 className="text-3xl font-bold text-gray-800 mb-2">任务清单</h1>
          <p className="text-gray-600">高效管理你的日常任务</p>
        </div>

        {/* Main Card */}
        <div className="bg-white rounded-2xl shadow-xl p-6">
          {/* Input */}
          <TodoInput onAdd={addTodo} />

          {/* Filter */}
          <div className="mb-4">
            <TodoFilter currentFilter={filter} onFilterChange={setFilter} />
          </div>

          {/* Todo List */}
          <TodoList
            todos={filteredTodos}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
            filter={filter}
          />

          {/* Stats */}
          <TodoStats
            total={stats.total}
            completed={stats.completed}
            active={stats.active}
            onClearCompleted={clearCompleted}
          />
        </div>

        {/* Footer */}
        <p className="text-center text-gray-500 text-sm mt-6">
          提示：按 Enter 键快速添加任务
        </p>
      </div>
    </div>
  );
}

export default App;
