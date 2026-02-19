import { motion } from 'framer-motion';
import { ClipboardList } from 'lucide-react';

interface EmptyStateProps {
  filter: 'all' | 'active' | 'completed';
}

export function EmptyState({ filter }: EmptyStateProps) {
  const messages = {
    all: {
      title: '还没有任务',
      description: '添加一个新任务开始管理你的待办事项吧！',
    },
    active: {
      title: '没有进行中的任务',
      description: '太棒了！所有任务都已完成 🎉',
    },
    completed: {
      title: '没有已完成的任务',
      description: '完成任务后会显示在这里',
    },
  };

  const message = messages[filter];

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      className="flex flex-col items-center justify-center py-12 text-center"
    >
      <div className="w-20 h-20 bg-gray-100 rounded-full flex items-center justify-center mb-4">
        <ClipboardList size={40} className="text-gray-400" />
      </div>
      <h3 className="text-lg font-medium text-gray-700 mb-2">{message.title}</h3>
      <p className="text-gray-500 max-w-xs">{message.description}</p>
    </motion.div>
  );
}
