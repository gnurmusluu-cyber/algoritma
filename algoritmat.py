import React, { useState } from 'react';
import { Play, X, GripVertical, CheckCircle, XCircle, Code } from 'lucide-react';

const AlgoritmaMat = () => {
  const [workspace, setWorkspace] = useState([]);
  const [testValues, setTestValues] = useState({ a: '', b: '', c: '' });
  const [result, setResult] = useState(null);
  const [showAnimation, setShowAnimation] = useState(false);

  const availableBlocks = [
    { id: 'input', label: 'Veri Al', color: 'bg-blue-500', code: 'a, b, c = input()' },
    { id: 'calculate', label: 'Hesapla', color: 'bg-purple-500', code: 'toplam = a + b\nfark = abs(a - b)' },
    { id: 'check', label: 'Eşitsizliği Kontrol Et', color: 'bg-green-500', code: 'if fark < c < toplam:' },
    { id: 'output', label: 'Sonucu Yazdır', color: 'bg-orange-500', code: '    print("Geçerli üçgen")' }
  ];

  const addBlock = (block) => {
    setWorkspace([...workspace, { ...block, uniqueId: Date.now() }]);
  };

  const removeBlock = (uniqueId) => {
    setWorkspace(workspace.filter(b => b.uniqueId !== uniqueId));
  };

  const moveBlock = (index, direction) => {
    const newWorkspace = [...workspace];
    const targetIndex = direction === 'up' ? index - 1 : index + 1;
    if (targetIndex >= 0 && targetIndex < workspace.length) {
      [newWorkspace[index], newWorkspace[targetIndex]] = [newWorkspace[targetIndex], newWorkspace[index]];
      setWorkspace(newWorkspace);
    }
  };

  const generatePythonCode = () => {
    if (workspace.length === 0) return '# Algoritma bloklarını sürükleyerek başlayın';
    return workspace.map(block => block.code).join('\n');
  };

  const runAlgorithm = () => {
    const a = parseFloat(testValues.a);
    const b = parseFloat(testValues.b);
    const c = parseFloat(testValues.c);

    if (isNaN(a) || isNaN(b) || isNaN(c)) {
      setResult({ success: false, message: 'Lütfen geçerli sayılar girin!' });
      return;
    }

    const toplam = a + b;
    const fark = Math.abs(a - b);
    const isValid = fark < c && c < toplam;

    setShowAnimation(true);
    setTimeout(() => {
      setResult({
        success: isValid,
        message: isValid 
          ? `✓ Başarılı! Bu kenarlar geçerli bir üçgen oluşturur.\n${fark.toFixed(1)} < ${c} < ${toplam.toFixed(1)}`
          : `✗ Hatalı! Bu kenarlar üçgen oluşturamaz.\nKural: |a-b| < c < a+b\n${fark.toFixed(1)} < ${c} < ${toplam.toFixed(1)} koşulu sağlanmıyor.`
      });
      setShowAnimation(false);
    }, 800);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-blue-600">Algorit-Mat</h1>
              <p className="text-sm text-slate-600 mt-1">Nitelikli Eğitim Laboratuvarı</p>
            </div>
            <div className="text-right">
              <div className="text-sm text-slate-500">İnteraktif Matematik Öğrenme</div>
              <div className="text-xs text-slate-400 mt-1">Algoritma & Mantık</div>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-6 py-8">
        {/* Math Concept Card */}
        <div className="bg-white rounded-xl shadow-md p-6 mb-8 border border-blue-100">
          <div className="flex items-start gap-4">
            <div className="bg-blue-100 rounded-lg p-3">
              <svg className="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
            <div className="flex-1">
              <h2 className="text-xl font-bold text-slate-800 mb-2">Üçgen Eşitsizliği Kuralı</h2>
              <p className="text-slate-600 mb-3">Bir üçgenin herhangi iki kenarının uzunlukları toplamı, üçüncü kenardan büyük olmalıdır.</p>
              <div className="bg-blue-50 rounded-lg p-4 border border-blue-200">
                <p className="text-center text-2xl font-bold text-blue-700 font-mono">|a - b| &lt; c &lt; a + b</p>
                <p className="text-center text-sm text-slate-600 mt-2">a, b, c üçgenin kenar uzunlukları</p>
              </div>
            </div>
          </div>
        </div>

        {/* Main Content Grid */}
        <div className="grid grid-cols-12 gap-6">
          {/* Block Selection */}
          <div className="col-span-3">
            <div className="bg-white rounded-xl shadow-md p-4 border border-slate-200">
              <h3 className="font-bold text-slate-800 mb-4 flex items-center gap-2">
                <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
                Algoritma Blokları
              </h3>
              <div className="space-y-3">
                {availableBlocks.map(block => (
                  <button
                    key={block.id}
                    onClick={() => addBlock(block)}
                    className={`w-full ${block.color} text-white rounded-lg p-3 text-sm font-medium hover:opacity-90 transition-all shadow-sm hover:shadow-md transform hover:scale-105`}
                  >
                    {block.label}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Workspace */}
          <div className="col-span-5">
            <div className="bg-white rounded-xl shadow-md p-4 border border-slate-200 min-h-96">
              <h3 className="font-bold text-slate-800 mb-4 flex items-center gap-2">
                <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
                Çalışma Alanı
              </h3>
              {workspace.length === 0 ? (
                <div className="flex items-center justify-center h-64 border-2 border-dashed border-slate-300 rounded-lg">
                  <p className="text-slate-400 text-center">
                    Soldan blokları seçerek<br />algoritmayı oluşturun
                  </p>
                </div>
              ) : (
                <div className="space-y-3">
                  {workspace.map((block, index) => (
                    <div key={block.uniqueId} className="group relative">
                      <div className={`${block.color} text-white rounded-lg p-3 flex items-center gap-3 shadow-sm`}>
                        <GripVertical className="w-4 h-4 opacity-50" />
                        <span className="flex-1 font-medium text-sm">{block.label}</span>
                        <div className="flex gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                          {index > 0 && (
                            <button
                              onClick={() => moveBlock(index, 'up')}
                              className="bg-white bg-opacity-20 hover:bg-opacity-30 rounded p-1"
                            >
                              ↑
                            </button>
                          )}
                          {index < workspace.length - 1 && (
                            <button
                              onClick={() => moveBlock(index, 'down')}
                              className="bg-white bg-opacity-20 hover:bg-opacity-30 rounded p-1"
                            >
                              ↓
                            </button>
                          )}
                          <button
                            onClick={() => removeBlock(block.uniqueId)}
                            className="bg-white bg-opacity-20 hover:bg-opacity-30 rounded p-1"
                          >
                            <X className="w-4 h-4" />
                          </button>
                        </div>
                      </div>
                      {index < workspace.length - 1 && (
                        <div className="flex justify-center my-1">
                          <div className="w-0.5 h-4 bg-slate-300"></div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Python Preview */}
          <div className="col-span-4">
            <div className="bg-slate-900 rounded-xl shadow-md p-4 border border-slate-700">
              <h3 className="font-bold text-slate-200 mb-4 flex items-center gap-2">
                <Code className="w-4 h-4 text-green-400" />
                Python Kodu
              </h3>
              <pre className="bg-slate-950 rounded-lg p-4 text-green-400 text-sm font-mono overflow-x-auto min-h-64">
                {generatePythonCode()}
              </pre>
            </div>
          </div>
        </div>

        {/* Simulation Test Area */}
        <div className="mt-8 bg-white rounded-xl shadow-md p-6 border border-slate-200">
          <h3 className="font-bold text-slate-800 mb-4 flex items-center gap-2">
            <Play className="w-5 h-5 text-blue-600" />
            Simülasyon Testi
          </h3>
          <div className="grid grid-cols-12 gap-6">
            <div className="col-span-8">
              <div className="flex gap-4 mb-4">
                <div className="flex-1">
                  <label className="block text-sm font-medium text-slate-700 mb-2">Kenar a</label>
                  <input
                    type="number"
                    value={testValues.a}
                    onChange={(e) => setTestValues({...testValues, a: e.target.value})}
                    className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Örn: 5"
                  />
                </div>
                <div className="flex-1">
                  <label className="block text-sm font-medium text-slate-700 mb-2">Kenar b</label>
                  <input
                    type="number"
                    value={testValues.b}
                    onChange={(e) => setTestValues({...testValues, b: e.target.value})}
                    className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Örn: 7"
                  />
                </div>
                <div className="flex-1">
                  <label className="block text-sm font-medium text-slate-700 mb-2">Kenar c</label>
                  <input
                    type="number"
                    value={testValues.c}
                    onChange={(e) => setTestValues({...testValues, c: e.target.value})}
                    className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="Örn: 10"
                  />
                </div>
              </div>
              <button
                onClick={runAlgorithm}
                disabled={workspace.length === 0}
                className="w-full bg-blue-600 text-white rounded-lg py-3 font-bold hover:bg-blue-700 transition-all disabled:bg-slate-300 disabled:cursor-not-allowed flex items-center justify-center gap-2 shadow-md hover:shadow-lg"
              >
                <Play className="w-5 h-5" />
                Algoritmayı Çalıştır
              </button>
            </div>
            <div className="col-span-4">
              {result && (
                <div className={`h-full rounded-lg p-4 border-2 flex flex-col items-center justify-center text-center ${
                  result.success 
                    ? 'bg-green-50 border-green-300' 
                    : 'bg-red-50 border-red-300'
                } ${showAnimation ? 'animate-pulse' : ''}`}>
                  {result.success ? (
                    <CheckCircle className="w-16 h-16 text-green-600 mb-3" />
                  ) : (
                    <XCircle className="w-16 h-16 text-red-600 mb-3" />
                  )}
                  <p className={`font-bold text-lg mb-2 ${result.success ? 'text-green-800' : 'text-red-800'}`}>
                    {result.success ? 'Başarılı!' : 'Hatalı!'}
                  </p>
                  <p className={`text-sm whitespace-pre-line ${result.success ? 'text-green-700' : 'text-red-700'}`}>
                    {result.message}
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AlgoritmaMat;
