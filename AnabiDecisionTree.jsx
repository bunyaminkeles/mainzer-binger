'use client';

import { useState } from 'react';
import {
  CheckCircle,
  XCircle,
  AlertTriangle,
  ChevronRight,
  RotateCcw,
  GraduationCap,
  Info,
} from 'lucide-react';

// ─── Data ──────────────────────────────────────────────────────────────────

const STEPS = {
  1: {
    id: 1,
    total: 3,
    question: 'Anabin veritabanında üniversitenizi buldunuz mu? Kurum statüsü nedir?',
    hint: 'anabin.kmk.org adresinden üniversitenizin adını aratın ve kurum kartında statüyü kontrol edin.',
    options: [
      { label: 'H+',          desc: 'Kurum tanınıyor',        next: 2,           color: 'green'  },
      { label: 'H-',          desc: 'Kurum tanınmıyor',       next: 'outcome-1', color: 'red'    },
      { label: 'H+/-',        desc: 'Kısmi tanınma',          next: 'outcome-2', color: 'yellow' },
      { label: 'Bulamadım',   desc: 'Listede yok',            next: 'outcome-2', color: 'yellow' },
    ],
  },
  2: {
    id: 2,
    total: 3,
    question: 'Harika! Okulunuz tanınıyor. Peki mezun olduğunuz bölüm (Abschluss), Anabin\'de birebir aynı isimle listelenmiş mi?',
    hint: 'Kurum sayfasında "Abschlüsse" sekmesine tıklayın ve lisansüstü / lisans bölümünüzü arayın.',
    options: [
      { label: 'Evet, listelenmiş',               desc: 'Bölümüm var',                 next: 3,           color: 'green'  },
      { label: 'Hayır, bölümüm yok / isim farklı', desc: 'Eşleşme bulunamadı',          next: 'outcome-3', color: 'yellow' },
    ],
  },
  3: {
    id: 3,
    total: 3,
    question: 'Bölümünüzün "Klasse" veya "Äquivalenzklasse" durumu nedir?',
    hint: 'Bölümünüzün detay satırında "Klasse" sütununu inceleyin.',
    options: [
      { label: 'Entspricht / Gleichwertig', desc: 'Tam denklik',           next: 'outcome-4', color: 'green'  },
      { label: 'Bedingt vergleichbar / Diğer', desc: 'Kısmi veya belirsiz', next: 'outcome-3', color: 'yellow' },
    ],
  },
};

const OUTCOMES = {
  'outcome-1': {
    Icon: XCircle,
    scheme: 'red',
    title: 'Üzgünüz, diplomanız tanınmıyor.',
    text: 'Kurumunuz H- statüsünde. Bu diploma ile Mavi Kart veya nitelikli çalışan vizesi alamazsınız. ZAB başvurusu da bu durumu değiştirmez.',
    action: null,
  },
  'outcome-2': {
    Icon: AlertTriangle,
    scheme: 'yellow',
    title: 'ZAB Başvurusu Zorunlu!',
    text: 'Okulunuzun durumu net değil veya sistemde yok. Diplomanızın geçerliliğini kanıtlamak için mutlaka ZAB\'a (Zeugnisbewertung) bireysel başvuru yapmalısınız.',
    action: { label: 'ZAB Rehberini Oku', href: 'https://zab.kmk.org/de/zeugnisbewertung/antrag' },
  },
  'outcome-3': {
    Icon: AlertTriangle,
    scheme: 'yellow',
    title: 'ZAB Başvurusu Zorunlu!',
    text: 'Okulunuz tanınsa da, bölümünüz Anabin\'de birebir eşleşmiyor. Vize sürecinde sorun yaşamamak için ZAB\'a (Zeugnisbewertung) başvurmalısınız.',
    action: { label: 'ZAB Başvuru Sürecini İncele', href: 'https://zab.kmk.org/de/zeugnisbewertung/antrag' },
  },
  'outcome-4': {
    Icon: CheckCircle,
    scheme: 'green',
    title: 'Tebrikler! ZAB Başvurusuna Gerek Yok.',
    text: 'Okulunuz (H+) ve bölümünüz tam olarak tanınıyor. Anabin\'den okulunuzun ve bölümünüzün ekran çıktılarını (PDF) alarak doğrudan vize / Mavi Kart başvurunuza ekleyebilirsiniz. ZAB\'a boşuna 200 Euro ödemeyin!',
    action: { label: 'Anabin\'e Git', href: 'https://anabin.kmk.org' },
  },
};

// ─── Colour tokens ─────────────────────────────────────────────────────────

const OPTION_STYLE = {
  green:  'border-emerald-200 hover:border-emerald-400 hover:bg-emerald-50',
  yellow: 'border-amber-200   hover:border-amber-400   hover:bg-amber-50',
  red:    'border-red-200     hover:border-red-400     hover:bg-red-50',
};

const OUTCOME_STYLE = {
  green:  { wrap: 'bg-emerald-50 border-emerald-200', icon: 'text-emerald-500', btn: 'bg-emerald-600 hover:bg-emerald-700' },
  yellow: { wrap: 'bg-amber-50  border-amber-200',   icon: 'text-amber-500',   btn: 'bg-amber-600  hover:bg-amber-700'  },
  red:    { wrap: 'bg-red-50    border-red-200',      icon: 'text-red-500',     btn: 'bg-red-600    hover:bg-red-700'    },
};

// ─── Sub-components ────────────────────────────────────────────────────────

function ProgressBar({ current, total }) {
  const pct = Math.round((current / total) * 100);
  return (
    <div className="mb-6">
      <div className="flex justify-between text-xs text-gray-400 mb-1">
        <span>Adım {current} / {total}</span>
        <span>{pct}%</span>
      </div>
      <div className="h-1.5 bg-gray-100 rounded-full overflow-hidden">
        <div
          className="h-full bg-indigo-500 rounded-full transition-all duration-500 ease-out"
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}

function StepCard({ step, onSelect, onBack, onReset, canGoBack }) {
  return (
    <>
      <ProgressBar current={step.id} total={step.total} />

      <h2 className="text-base font-semibold text-gray-800 leading-snug mb-3">
        {step.question}
      </h2>

      {step.hint && (
        <div className="flex items-start gap-2 bg-indigo-50 text-indigo-700 text-xs p-3 rounded-lg mb-4">
          <Info size={14} className="mt-0.5 shrink-0" />
          <span>{step.hint}</span>
        </div>
      )}

      <div className="space-y-2.5 mb-5">
        {step.options.map((opt) => (
          <button
            key={opt.label}
            onClick={() => onSelect(opt.next)}
            className={`w-full text-left border-2 rounded-xl px-4 py-3.5 transition-all duration-150 group ${OPTION_STYLE[opt.color]}`}
          >
            <div className="flex items-center justify-between gap-3">
              <div>
                <span className="font-semibold text-gray-800 text-sm">{opt.label}</span>
                {opt.desc && (
                  <span className="text-xs text-gray-500 ml-1.5">— {opt.desc}</span>
                )}
              </div>
              <ChevronRight
                size={16}
                className="text-gray-400 shrink-0 group-hover:translate-x-0.5 transition-transform"
              />
            </div>
          </button>
        ))}
      </div>

      <div className="flex gap-2 pt-3 border-t border-gray-100">
        {canGoBack && (
          <button
            onClick={onBack}
            className="flex-1 text-sm text-gray-500 hover:text-gray-700 py-2 transition-colors"
          >
            ← Geri
          </button>
        )}
        <button
          onClick={onReset}
          className="flex-1 flex items-center justify-center gap-1.5 text-sm text-gray-400 hover:text-gray-600 py-2 transition-colors"
        >
          <RotateCcw size={13} />
          Başa Dön
        </button>
      </div>
    </>
  );
}

function OutcomeCard({ outcome, onReset }) {
  const { Icon, scheme, title, text, action } = outcome;
  const s = OUTCOME_STYLE[scheme];

  return (
    <>
      <div className={`border rounded-xl p-5 mb-5 ${s.wrap}`}>
        <div className="flex items-start gap-3">
          <Icon size={26} className={`${s.icon} shrink-0 mt-0.5`} />
          <div>
            <h3 className="font-bold text-gray-800 text-base mb-1">{title}</h3>
            <p className="text-gray-600 text-sm leading-relaxed">{text}</p>
          </div>
        </div>
      </div>

      <div className="space-y-2">
        {action && (
          <a
            href={action.href}
            target="_blank"
            rel="noopener noreferrer"
            className={`flex items-center justify-center gap-2 w-full text-white text-sm font-medium py-3 rounded-xl transition-colors ${s.btn}`}
          >
            {action.label}
            <ChevronRight size={16} />
          </a>
        )}
        <button
          onClick={onReset}
          className="w-full flex items-center justify-center gap-1.5 text-sm text-gray-400 hover:text-gray-600 py-2 transition-colors"
        >
          <RotateCcw size={13} />
          Başa Dön
        </button>
      </div>
    </>
  );
}

// ─── Main component ────────────────────────────────────────────────────────

export default function AnabiDecisionTree() {
  const [current, setCurrent] = useState(1);
  const [history, setHistory] = useState([]);
  const [visible, setVisible] = useState(true);

  const transition = (fn) => {
    setVisible(false);
    setTimeout(() => {
      fn();
      setVisible(true);
    }, 180);
  };

  const navigate = (next) => transition(() => {
    setHistory((h) => [...h, current]);
    setCurrent(next);
  });

  const goBack = () => transition(() => {
    setCurrent(history[history.length - 1]);
    setHistory((h) => h.slice(0, -1));
  });

  const reset = () => transition(() => {
    setCurrent(1);
    setHistory([]);
  });

  const isOutcome = typeof current === 'string';

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-100 to-indigo-100 flex items-center justify-center p-4">
      <div className="w-full max-w-md">

        {/* Header */}
        <div className="text-center mb-5">
          <div className="inline-flex items-center gap-2 text-indigo-700 font-bold text-lg">
            <GraduationCap size={22} />
            Anabin Karar Aracı
          </div>
          <p className="text-xs text-gray-500 mt-1">
            ZAB Zeugnisbewertung başvurusu gerekli mi?
          </p>
        </div>

        {/* Card */}
        <div
          className={`bg-white rounded-2xl shadow-md p-6 transition-opacity duration-200 ${
            visible ? 'opacity-100' : 'opacity-0'
          }`}
        >
          {isOutcome ? (
            <OutcomeCard outcome={OUTCOMES[current]} onReset={reset} />
          ) : (
            <StepCard
              step={STEPS[current]}
              onSelect={navigate}
              onBack={goBack}
              onReset={reset}
              canGoBack={history.length > 0}
            />
          )}
        </div>

        {/* Footer */}
        <p className="text-center text-xs text-gray-400 mt-4">
          Bu araç bilgi amaçlıdır. Nihai karar için yetkili danışman görüşü alın.
        </p>
      </div>
    </div>
  );
}
