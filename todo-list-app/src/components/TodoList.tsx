import { AnimatePresence } from 'framer-motion';
import { TodoItem } from './TodoItem';
import { EmptyState } from './EmptyState';
import type { Todo } from '../types/todo';

interface TodoListProps {
  todos: Todo[];
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
  filter: 'all' | 'active' | 'completed';
}

export function TodoList({ todos, onToggle, onDelete, filter }: TodoListProps) {
  if (todos.length === 0) {
    return <EmptyState filter={filter} />;
  }

  return (
    <div className="space-y-2">
      <AnimatePresence mode="popLayout">
        {todos.map((todo) => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onToggle={() => onToggle(todo.id)}
            onDelete={() => onDelete(todo.id)}
          />
        ))}
      </AnimatePresence>
    </div>
  );
}
