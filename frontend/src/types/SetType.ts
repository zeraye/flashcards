import type { CardType } from './CardType'

export type SetType = {
  id: string
  title: string
  description: string
  term_locale_code: string
  definition_locale_code: string
  flashcards: Array<CardType>
}
