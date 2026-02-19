interface TodoStatsProps {
  total: number;
  completed: number;
  active: number;
  onClearCompleted: () => void;
}

export function TodoStats({ total, completed, active, onClearCompleted }: TodoStatsProps) {
  if (total === 0) return null;

  return (
    <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 py-4 text-sm text-gray-600 border-t border-gray-200">
      <div className="flex gap-4">
        <span>总计: <strong className="text-gray-800">{total}</strong></span>
        <span>进行中: <strong className="text-blue-600">{active}</strong></span>
        <span>已完成: <strong className="text-green-600">{completed}</strong></span>
      </div>
      
      {completed > 0 && (
        <button
          onClick={onClearCompleted}
          className="text-red-500 hover:text-red-600 hover:underline transition-colors text-left sm:text-right"
        >
          清除已完成 ({completed})
        </button>
      )}
    </div>
  );
}
