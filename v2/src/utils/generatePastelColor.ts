export function generatePastelColor(): string {
  // Genera valores altos para R, G, B y los mezcla con blanco para suavizar el color
  const r = Math.round(Math.random() * 127 + 127);
  const g = Math.round(Math.random() * 127 + 127);
  const b = Math.round(Math.random() * 127 + 127);
  return `#${((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1)}`;
}
