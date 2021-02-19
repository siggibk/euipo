import { Typography } from "@material-ui/core"
import { TrademarkText } from "./TrademarkText";

export const TrademarkApplication = ({ trademark }) => {
  return (
    <div>
      <Typography color="textSecondary" variant="h4" component="h4">
        {trademark.name}
      </Typography>
      <TrademarkText
        label="Trademark name"
        text={trademark.name}
      />
      <TrademarkText
        label="Application number"
        text={trademark.application_number}
      />
      <TrademarkText
        label="Applicant identifier"
        text={trademark.applicant_identifier}
      />
      <TrademarkText
        label="Representative identifier"
        text={trademark.representative_identifier}
      />
      <TrademarkText
        label="Application date"
        text={trademark.application_date}
      />
      <TrademarkText
        label="Registration date"
        text={trademark.registration_date}
      />
      <TrademarkText
        label="Application status"
        text={trademark.status}
      />
      <TrademarkText
        label="Status milestone"
        text={trademark.status_milestone}
      />
      <TrademarkText
        label="Status date"
        text={trademark.status_date}
      />
      <TrademarkText
        label="Expiry date"
        text={trademark.expiry_date}
      />
    </div>   
  )
}